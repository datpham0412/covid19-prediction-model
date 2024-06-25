#include "../include/data_processor.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <SQLiteCpp/SQLiteCpp.h>

void DataProcessor::loadCSV(const std::string &fileName)
{
    std::ifstream file(fileName);
    if (!file.is_open())
    {
        throw std::runtime_error("Unable to open file " + fileName);
    }
    std::string line;
    std::getline(file, line);        // Skip the header
    while (std::getline(file, line)) // Reads the first data line: "Afghanistan,2020-01-05,,,,0.0,0.0,,41128772.0"
    {
        std::vector<std::string> row;
        std::stringstream ss(line); // ss contains: "Afghanistan,2020-01-05,,,,0.0,0.0,,41128772.0"
        std::string value;
        while (std::getline(ss, value, ',')) // Reads each value separated by commas
        {
            row.push_back(value); // Add each value to the row vector
        }
        data.push_back(row); // Adds the row vector to the data vector
    }
}

void DataProcessor::processData()
{
    // Example: Process data, e.g., normalize values, handle missing data
    for (auto &row : data)
    {
        for (auto &value : row)
        {
            // Perform some processing on each value
        }
    }
}

void DataProcessor::saveToDatabase(const std::string &db_fileName)
{
    // Open or create a database file specified by db_fileName:
    SQLite::Database db(db_fileName, SQLite::OPEN_READWRITE | SQLite::OPEN_CREATE);

    // Drop the existing Data table if it exists
    db.exec("DROP TABLE IF EXISTS Data");

    // Create a new data table with the specified columns
    db.exec("CREATE TABLE Data (id INTEGER PRIMARY KEY, location TEXT, date TEXT, total_cases REAL, total_deaths REAL, total_tests REAL, new_cases REAL, new_deaths REAL, new_tests REAL, population REAL)");

    // Begin a transaction on the database:
    SQLite::Transaction transaction(db);

    // Iterate over each row in the data vector
    for (const auto &row : data)
    {
        // Prepare an SQL statement to insert a new row into the Data table
        SQLite::Statement query(db, "INSERT INTO Data (location, date, total_cases, total_deaths, total_tests, new_cases, new_deaths, new_tests, population) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)");

        // Bind the values from row vector to the SQL statement
        query.bind(1, row[0]); // Bind location
        query.bind(2, row[1]); // Bind date
        query.bind(3, row[2]); // Bind total_cases
        query.bind(4, row[3]); // Bind total_deaths
        query.bind(5, row[4]); // Bind total_tests
        query.bind(6, row[5]); // Bind new_cases
        query.bind(7, row[6]); // Bind new_deaths
        query.bind(8, row[7]); // Bind new_tests
        query.bind(9, row[8]); // Bind population

        // Execute the prepared SQL statement to insert the new row into the database
        query.exec();
    }
    // Commit the transaction to apply all changes to the database
    transaction.commit();
}