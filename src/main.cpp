#include "../include/data_processor.h"
#include <iostream>
#include <filesystem>

int main()
{
    try
    {
        // Ensure the db directory exists
        std::filesystem::path db_directory("../../data/db");
        if (!std::filesystem::exists(db_directory))
        {
            std::filesystem::create_directories(db_directory);
        }

        DataProcessor dp;
        dp.loadCSV("../../data/processed/covid_data_aus.csv", false);
        dp.loadCSV("../../data/processed/mobility_data_aus.csv", true);
        dp.processData();
        dp.saveToDatabase("../../data/db/processed_data_aus.db");
    }
    catch (const std::exception &e)
    {
        std::cerr << "Exception: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
