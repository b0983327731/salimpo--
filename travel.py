import tkinter as tk
from tkinter import messagebox, font

class NingpuAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NINGPU Voyager v9.0")
        self.root.geometry("400x700")
        self.root.configure(bg='#0055A4')  # 長濱藍

        # --- [修正點] 強制定義支援中文的字體清單 ---
        # 遍歷性原則：嘗試多種系統字體，確保在 Mac/Windows/Linux 都不會亂碼
        self.title_font = self.get_safe_font(18, True)
        self.card_font = self.get_safe_font(12, True)
        self.desc_font = self.get_safe_font(10, False)

        # 1. 頂部導航
        self.header = tk.Frame(self.root, bg='#0055A4', pady=20)
        self.header.pack(fill='x')
        tk.Label(self.header, text="長濱寧埔 | AWOS 農場", 
                 fg='#F5D105', bg='#0055A4', font=self.title_font).pack()

        # 2. 模擬視覺區 (視覺降熵)
        self.hero = tk.Frame(self.root, bg='#003366', height=200)
        self.hero.pack(fill='x', padx=15, pady=10)
        self.hero.pack_propagate(False)
        tk.Label(self.hero, text="【 太平洋 S 彎道景觀 】\n(影像預載中...)", 
                 fg='white', bg='#003366', font=self.desc_font).place(relx=0.5, rely=0.5, anchor='center')

        # 3. 核心功能按鈕 (Tier 1: Conversion Hotzone)
        self.btn = tk.Button(self.root, text="立即預約 AWOS 職人體驗", 
                             command=self.book_action,
                             bg='#F5D105', fg='#000000', 
                             font=self.card_font, bd=0, padx=20, pady=10)
        self.btn.pack(pady=20)

        # 4. 景點介紹卡片 (低認知負荷)
        self.render_card("AWOS 農場", "自然農法、紅藜與傳統海鹽體驗")
        self.render_card("寧埔休憩區", "全台最美海岸線 S 彎道攝影點")
        self.render_card("光榮部落", "探訪阿美族傳統智慧與文化遺址")

    def get_safe_font(self, size, is_bold):
        # 自動偵測系統環境，避免亂碼
        weight = "bold" if is_bold else "normal"
        # 優先順序：微軟正黑體 (Win), 蘋方 (Mac), 文鼎 (Linux), 系統預設
        for f in ["Microsoft JhengHei", "PingFang TC", "Noto Sans TC", "Arial Unicode MS"]:
            if f in font.families():
                return font.Font(family=f, size=size, weight=weight)
        return font.Font(size=size, weight=weight)

    def render_card(self, title, desc):
        card = tk.Frame(self.root, bg='#003366', padx=15, pady=10)
        card.pack(fill='x', padx=15, pady=5)
        tk.Label(card, text=title, fg='#F5D105', bg='#003366', font=self.card_font).pack(anchor='w')
        tk.Label(card, text=desc, fg='white', bg='#003366', font=self.desc_font).pack(anchor='w')

    def book_action(self):
        messagebox.showinfo("預約成功", "已為您保留 AWOS 農場體驗名額！\n系統正同步至長濱在地伺服器...")

if __name__ == "__main__":
    root = tk.Tk()
    app = NingpuAppGUI(root)
    root.mainloop()
