// ============================================================================
// main.cpp - HuyEngine Application Entry Point
// ============================================================================
#include <iostream>
#include "Core/Engine.h"

int main() {
    HuyEngine::SayHello();

    HuyEngine::Engine engine;
    engine.Run();
    std::cin.get();
    return 0;
}
