#ifndef DATA_PROCESSOR_H
#define DATA_PROCESSOR_H

#include <string>
#include <vector>

class DataProcessor
{
public:
    void loadCSV(const std::string &filename);
    void processData();
    void saveToDatabase(const std::string &db_filename);

private:
    std::vector<std::vector<std::string>> data;
};

#endif // DATA_PROCESSOR_H
