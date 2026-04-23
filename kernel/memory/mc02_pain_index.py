import json
import os

class MC02PainIndex:
    def __init__(self, storage_file="kernel/mc_core/pain_index_data.json"):
        """
        MC-02 痛覺索引系統
        storage_file: 記憶實體化存入硬碟的 JSON 檔案路徑。
        """
        self.storage_file = storage_file
        self.minor_roadblocks = {}   # 次要錯誤 (路障): { "路徑": 阻力值 }
        self.critical_firewalls = set() # 嚴重錯誤 (禁區): { "路徑" }
        self._load_memory()

    def _load_memory(self):
        """啟動時讀取存儲於硬碟的痛覺記憶"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.minor_roadblocks = data.get("minor", {})
                self.critical_firewalls = set(data.get("critical", []))
            except (json.JSONDecodeError, IOError):
                print("[MC-02] 記憶讀取異常，系統將建立全新索引。")

    def _save_memory(self):
        """將當前記憶同步至實體檔案"""
        os.makedirs(os.path.dirname(self.storage_file), exist_ok=True)
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "minor": self.minor_roadblocks,
                    "critical": list(self.critical_firewalls)
                }, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"[MC-02] 寫入記憶失敗: {e}")

    def record_minor(self, path, penalty=0.1):
        """記錄次要錯誤。路障阻力上限為 1.0"""
        current_penalty = self.minor_roadblocks.get(path, 0.0)
        self.minor_roadblocks[path] = min(1.0, current_penalty + penalty)
        self._save_memory()
        print(f"[MC-02] 標記路障: {path} (當前阻力: {self.minor_roadblocks[path]:.2f})")

    def record_critical(self, path):
        """記錄災難性錯誤。直接寫入防火牆，永久封鎖該路徑"""
        self.critical_firewalls.add(path)
        self._save_memory()
        print(f"[MC-02] 🚨 建立禁區防火牆: {path}")

    def evaluate_path(self, path):
        """
        評估路徑安全性。
        回傳: (is_safe, penalty)
        """
        if path in self.critical_firewalls:
            return False, 1.0
        
        penalty = self.minor_roadblocks.get(path, 0.0)
        return True, penalty
