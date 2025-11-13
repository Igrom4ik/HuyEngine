//
// Created by igrom on 13.11.2025.
//

#include "Engine.h"
#include <iostream>

namespace HuyEngine {
    void SayHello() {
        std::cout << "Hello from HuyEngine!" << std::endl;
    }

    void Engine::Run() {
        std::cout << "Engine is running..." << std::endl;
    }
}
