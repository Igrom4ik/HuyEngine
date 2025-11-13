// ============================================================================
// main.cpp - HuyEngine Application Entry Point
// ============================================================================

import Engine;

int main() {
    // Call function from module
    HuyEngine::SayHello();

    // Use class from module
    HuyEngine::Engine engine;
    engine.Run();

    return 0;
}
