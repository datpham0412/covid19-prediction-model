#include "../include/data_processor.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <SQLiteCpp/SQLiteCpp.h>
#include <chrono>
#include <vector>
#include <stdexcept>

void DataProcessor::loadCSV(const std::string &fileName, bool isMobility)
{
    auto start = std::chrono::high_resolution_clock::now();

    std::ifstream file(fileName);
    if (!file.is_open())
    {
        throw std::runtime_error("Unable to open file " + fileName);
    }

    std::string line;
    std::getline(file, line);        // Skip the header
    while (std::getline(file, line)) // Read each data line
    {
        std::vector<std::string> row;
        std::stringstream ss(line);
        std::string value;
        while (std::getline(ss, value, ','))
        {
            row.push_back(value);
        }

        if (isMobility)
        {
            mobility_data.push_back(row);
        }
        else
        {
            covid_data.push_back(row);
        }
    }

    file.close();

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "Loaded " << (isMobility ? "mobility" : "covid") << " data in " << duration.count() << " seconds." << std::endl;
}

void DataProcessor::processData()
{
    auto start = std::chrono::high_resolution_clock::now();

    // Example: Process data, e.g., normalize values, handle missing data
    for (auto &row : covid_data)
    {
        for (auto &value : row)
        {
            // Perform some processing on each value (currently a placeholder)
        }
    }
    for (auto &row : mobility_data)
    {
        for (auto &value : row)
        {
            // Perform some processing on each value (currently a placeholder)
        }
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "Processed data in " << duration.count() << " seconds." << std::endl;
}

void DataProcessor::saveToDatabase(const std::string &db_fileName)
{
    auto start = std::chrono::high_resolution_clock::now();

    try
    {
        // Open or create a database file specified by db_fileName
        SQLite::Database db(db_fileName, SQLite::OPEN_READWRITE | SQLite::OPEN_CREATE);

        // Drop the existing CovidData table if it exists and create a new one
        db.exec("DROP TABLE IF EXISTS CovidData");
        db.exec("CREATE TABLE CovidData (id INTEGER PRIMARY KEY, location TEXT, date TEXT, total_cases REAL, total_deaths REAL, total_tests REAL, new_cases REAL, new_deaths REAL, new_tests REAL, population REAL)");

        // Drop the existing MobilityData table if it exists and create a new one
        db.exec("DROP TABLE IF EXISTS MobilityData");
        db.exec("CREATE TABLE MobilityData (id INTEGER PRIMARY KEY, country_region TEXT, sub_region_1 TEXT, sub_region_2 TEXT, date TEXT, retail_and_recreation REAL, grocery_and_pharmacy REAL, parks REAL, transit_stations REAL, workplaces REAL, residential REAL)");

        // Begin a transaction to ensure data consistency
        SQLite::Transaction transaction(db);

        // Insert rows into the CovidData table
        for (const auto &row : covid_data)
        {
            SQLite::Statement query(db, "INSERT INTO CovidData (location, date, total_cases, total_deaths, total_tests, new_cases, new_deaths, new_tests, population) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)");
            query.bind(1, row[0]); // Bind location
            query.bind(2, row[1]); // Bind date
            query.bind(3, row[2]); // Bind total_cases
            query.bind(4, row[3]); // Bind total_deaths
            query.bind(5, row[4]); // Bind total_tests
            query.bind(6, row[5]); // Bind new_cases
            query.bind(7, row[6]); // Bind new_deaths
            query.bind(8, row[7]); // Bind new_tests
            query.bind(9, row[8]); // Bind population
            query.exec();          // Execute the query to insert the row
        }

        // Insert rows into the MobilityData table
        for (const auto &row : mobility_data)
        {
            if (row.size() > 14)
            {
                SQLite::Statement query(db, "INSERT INTO MobilityData (country_region, sub_region_1, sub_region_2, date, retail_and_recreation, grocery_and_pharmacy, parks, transit_stations, workplaces, residential) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
                query.bind(1, row[1]);   // Bind country_region
                query.bind(2, row[2]);   // Bind sub_region_1
                query.bind(3, row[3]);   // Bind sub_region_2
                query.bind(4, row[8]);   // Bind date (corrected index)
                query.bind(5, row[9]);   // Bind retail_and_recreation
                query.bind(6, row[10]);  // Bind grocery_and_pharmacy
                query.bind(7, row[11]);  // Bind parks
                query.bind(8, row[12]);  // Bind transit_stations
                query.bind(9, row[13]);  // Bind workplaces
                query.bind(10, row[14]); // Bind residential
                query.exec();            // Execute the query to insert the row
            }
        }

        // Commit the transaction to apply all changes to the database
        transaction.commit();

        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> duration = end - start;
        std::cout << "Saved data to database in " << duration.count() << " seconds." << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
}