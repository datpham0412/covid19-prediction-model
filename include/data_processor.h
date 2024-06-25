#ifndef DATA_PROCESSOR_H
#define DATA_PROCESSOR_H

#include <vector>
#include <string>

class DataProcessor
{
private:
    std::vector<std::vector<std::string>> covid_data;
    std::vector<std::vector<std::string>> mobility_data;

public:
    void loadCSV(const std::string &fileName, bool isMobility);
    void processData();
    void saveToDatabase(const std::string &db_fileName);
};

#endif // DATA_PROCESSOR_H
