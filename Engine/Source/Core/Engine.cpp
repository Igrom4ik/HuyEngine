#include "Engine.hpp"
#include <iostream>

using namespace HuyEngine;

HuyEngine::Engine::Engine() {
    std::cout << "Hellow, I'm HuyEngine v" << version() << std::endl;
}
