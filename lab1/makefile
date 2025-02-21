CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17

SRC_DIR = src
CORE_DIR = core
IO_DIR = io
UTIL_DIR = util
OBJ_DIR = obj
BIN_DIR = bin

SRC = $(SRC_DIR)/main.cpp $(SRC_DIR)/$(UTIL_DIR)/Utils.cpp $(SRC_DIR)/$(IO_DIR)/MatrixReader.cpp
OBJ = $(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(SRC))
TARGET = $(BIN_DIR)/main

all: $(TARGET)

$(TARGET): $(OBJ)
	@mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) $^ -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIRS)
	@mkdir -p $(dir $@)  
	$(CXX) $(CXXFLAGS) -c $< -o $@

OBJ_DIRS:
	@mkdir -p $(OBJ_DIR) $(OBJ_DIR)/$(UTIL_DIR) $(OBJ_DIR)/$(IO_DIR) $(OBJ_DIR)/$(CORE_DIR)

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)
