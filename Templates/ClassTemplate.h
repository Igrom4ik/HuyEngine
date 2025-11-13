// ============================================================================
// ClassName.h - Brief description
// ============================================================================
#pragma once
namespace HuyEngine {
/// @brief Brief class description
class ClassName {
public:
    ClassName();
    ~ClassName();
    /// @brief Method description
    void DoSomething();
private:
    // Private members
    // Запретить копирование (опционально)
    ClassName(const ClassName&) = delete;
    ClassName& operator=(const ClassName&) = delete;
};
} // namespace HuyEngine

