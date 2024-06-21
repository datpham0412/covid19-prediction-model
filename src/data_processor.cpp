#include "../include/data_processor.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <SQLiteCpp/SQLiteCpp.h>

void DataProcessor::loadCSV(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        throw std::runtime_error("Unable to open file: " + filename);
    }
    std::string line;
    while (std::getline(file, line)) {
        std::vector<std::string> row;
        std::stringstream ss(line);
        std::string value;
        while (std::getline(ss, value, ',')) {
            row.push_back(value);
        }
        data.push_back(row);
    }
}

void DataProcessor::processData() {
    // Example: Process data, e.g., normalize values, handle missing data
    for (auto& row : data) {
        for (auto& value : row) {
            // Perform some processing on each value
        }
    }
}

void DataProcessor::saveToDatabase(const std::string& db_filename) {
    SQLite::Database db(db_filename, SQLite::OPEN_READWRITE | SQLite::OPEN_CREATE);
    db.exec("DROP TABLE IF EXISTS Data");
    db.exec("CREATE TABLE Data (id INTEGER PRIMARY KEY, column1 TEXT, column2 TEXT)");

    SQLite::Transaction transaction(db);
    for (const auto& row : data) {
        SQLite::Statement query(db, "INSERT INTO Data (column1, column2) VALUES (?, ?)");
        query.bind(1, row[0]);
        query.bind(2, row[1]);
        query.exec();
    }
    transaction.commit();
}
