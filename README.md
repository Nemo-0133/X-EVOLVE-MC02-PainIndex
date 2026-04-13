
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

​🌐 English Annotation / Developer Notes
​System Purpose
​MC-02 serves as the Negative Experience Reservoir for the X-EVOLVE architecture. Its primary objective is to transform system failures and logical conflicts into "Pain Signals" that the AI can remember and avoid in future iterations.
​Key Mechanisms
​Path Evaluation: Before executing any exploratory action, the system queries MC-02 to check if the intended path has a history of failure.
​Roadblocks (Minor Errors): These represent non-fatal setbacks (e.g., API timeouts). They increase the "Resistance" of a specific logic path without completely blocking it, encouraging the AI to find more efficient alternatives.
​Firewalls (Critical Errors): These represent system-threatening failures (e.g., memory overflows or core logic corruption). These paths are permanently blacklisted to ensure survival.
​Core Philosophy
​"Pain is not just a signal of damage; it is a map of where not to go, guiding the system toward genuine evolution."
