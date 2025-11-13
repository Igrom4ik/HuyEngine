//
// Created by igrom on 13.11.2025.
//

module;

#include <iostream>

export module Engine;

namespace HuyEngine {
    export void SayHello() {
        std::cout << "Hello from HuyEngine module!" << std::endl;
        std::cout.flush();
    }

    export class Engine {
    public:
        void Run() {
            std::cout << "Engine is running..." << std::endl;
            std::cout.flush();
        }
    };
} // namespace HuyEngine

