
# Compiler
CXX := g++
CXXFLAGS := -std=c++20 -Wall -Wextra -O2

# Find all nested include dirs named 'include'
INCLUDE_DIRS := include/
CXXFLAGS += $(addprefix -I, $(INCLUDE_DIRS)) 
# Libraries
LDLIBS := -lpaho-mqttpp3 -lpaho-mqtt3as -pthread


# Files
DAEMON_SRC := src/main.cpp
CLI_SRC := src/main_cli.cpp 

DAEMON_OBJ := build/main.o 
CLI_OBJ := build/main_cli.o 

DAEMON_OUT := build/main
CLI_OUT := build/cli 

.PHONY: all clean bear

daemon: $(DAEMON_OUT)

cli: $(CLI_OUT)

all: daemon cli

# Link object file to create binary
$(DAEMON_OUT): $(DAEMON_OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDLIBS)

$(CLI_OUT): $(CLI_OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDLIBS)

# Compile source to object
build/%.o: src/%.cpp | build
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Ensure build directory exists
build:
	mkdir -p build

# Generate compile_commands.json using bear
bear:
	bear -- make clean all

clean:
	rm -rf build
	rm -f compile_commands.json
