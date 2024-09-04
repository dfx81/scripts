all: clean compile-lib compile-bin run

build: build-lib build-bin

build-bin: build-linux build-win

build-lib: build-lib-linux build-lib-win

build-win:
	@mkdir -p bin
	@x86_64-w64-mingw32-g++ -Wall -g -Wextra -Werror -pedantic -O3 -s -std=c++11 -Wl,-R -Wl,'$$ORIGIN' ./src/*.cc -I. -L./bin -lmain -o bin/main.exe

build-linux:
	@mkdir -p bin
	@g++ -Wall -g -Wextra -Werror -pedantic -O3 -s -std=c++11 -Wl,-R -Wl,'$$ORIGIN' ./src/*.cc -I. -L./bin -lmain -o bin/main

build-lib-linux:
	@mkdir -p bin
	@g++ -Wall -g -Wextra -Werror -pedantic -O3 -shared -s -std=c++11 ./lib/*.cc -o bin/libmain.so

build-lib-win:
	@mkdir -p bin
	@x86_64-w64-mingw32-g++ -Wall -g -Wextra -Werror -pedantic -O3 -shared -s -std=c++11 ./lib/*.cc -o bin/main.dll

compile-bin:
	@mkdir -p bin
	@gcc -Wall -g -Wextra -Werror -pedantic -std=c++11 -Wl,-R -Wl,'$$ORIGIN' ./src/*.cc -I. -L./bin -lmain -o bin/main

compile-lib:
	@mkdir -p bin
	@gcc -Wall -g -Wextra -Werror -pedantic -shared -std=c++11 ./lib/*.cc -o bin/libmain.so

run:
	@bin/main

clean:
	@rm -rf bin
	@clear
