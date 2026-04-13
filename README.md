
# X-EVOLVE: MC-02 Pain Index System

### 📌 功能定位
MC-02 是系統的「痛覺過濾與記憶」層。它不負責決策，只負責記住「哪些路徑會痛」。

### 🛠 使用方法
1. **DE 模組執行前檢查**：呼叫 `evaluate_path(path)`。
2. **遇到小挫折 (API Timeout 等)**：呼叫 `record_minor(path)`。
3. **遇到系統崩潰/死鎖**：呼叫 `record_critical(path)`。

### 💾 儲存格式
記憶會自動生成於 `kernel/memory/pain_index_data.json`。
如需「格式化記憶」，直接刪除該 JSON 檔案即可。
