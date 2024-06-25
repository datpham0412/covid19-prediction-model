#include "../include/data_processor.h"
#include <iostream>

int main()
{
    DataProcessor dp;
    try
    {
        dp.loadCSV("../../data/covid_data_aus.csv", false);
        dp.loadCSV("../../data/mobility_data_aus.csv", true);
        dp.processData();
        dp.saveToDatabase("../../data/processed_data_aus.db");
    }
    catch (const std::exception &e)
    {
        std::cerr << "Exception: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
