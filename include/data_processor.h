#ifndef DATA_PROCESSOR_H
#define DATA_PROCESSOR_H

#include <vector>
#include <string>

class DataProcessor
{
private:
    std::vector<std::vector<std::string>> data;

public:
    void loadCSV(const std::string &fileName);
    void processData();
    void saveToDatabase(const std::string &db_fileName);
};

#endif // DATA_PROCESSOR_H