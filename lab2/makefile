CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iinclude
SRC = src/main.cpp src/Equation.cpp src/Solver.cpp src/Method.cpp
OBJ = $(SRC:.cpp=.o)
EXEC = nonlinear_solver

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)