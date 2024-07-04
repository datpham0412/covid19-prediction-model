#include "../include/data_processor.h"
#include <iostream>
#include <filesystem>
#include <string>

int main()
{
    try
    {
        // Ask the user for the country name
        std::string country;
        std::cout << "Enter the country name: ";
        std::cin >> country;

        // Ensure the db directory exists
        std::filesystem::path db_directory("../../data/db");
        if (!std::filesystem::exists(db_directory))
        {
            std::filesystem::create_directories(db_directory);
        }

        // Construct the file paths based on the user input
        std::string covid_data_file = "../../data/processed/covid_data_" + country + ".csv";
        std::string mobility_data_file = "../../data/processed/mobility_data_" + country + ".csv";
        std::string db_file = "../../data/db/processed_data_" + country + ".db";

        // Ensure the files exist
        if (!std::filesystem::exists(covid_data_file))
        {
            std::cerr << "Covid data file not found: " << covid_data_file << std::endl;
            return 1;
        }

        if (!std::filesystem::exists(mobility_data_file))
        {
            std::cerr << "Mobility data file not found: " << mobility_data_file << std::endl;
            return 1;
        }

        DataProcessor dp;
        dp.loadCSV(covid_data_file, false);
        dp.loadCSV(mobility_data_file, true);
        dp.processData();
        dp.saveToDatabase(db_file);
    }
    catch (const std::exception &e)
    {
        std::cerr << "Exception: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
