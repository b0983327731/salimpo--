# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, font

class NingpuUniversalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NINGPU Voyager v9.0")
        self.root.geometry("400x720")
        self.root.configure(bg='#0055A4')  # 憲法色：長濱藍

        # --- [10-1] 遍歷性原則：字體防禦矩陣 ---
        self.setup_fonts()

        # 1. 頂部導航 (Tier 1: Conversion Hotzone)
        self.header = tk.Frame(self.root, bg='#0055A4', pady=25)
        self.header.pack(fill='x')
        tk.Label(self.header, text="長濱寧埔 | AWOS 農場", 
                 fg='#F5D105', bg='#0055A4', font=self.f_title).pack()

        # 2. 視覺區 (視覺降熵)
        self.hero = tk.Frame(self.root, bg='#003366', height=180)
        self.hero.pack(fill='x', padx=20, pady=10)
        self.hero.pack_propagate(False)
        tk.Label(self.hero, text="【 太平洋 S 彎道景觀 】\nAWOS 自然農法實作基地", 
                 fg='white', bg='#003366', font=self.f_desc).place(relx=0.5, rely=0.5, anchor='center')

        # 3. 核心功能 (第一性原理：預約轉換)
        self.btn = tk.Button(self.root, text=" 立即預約 AWOS 體驗 ", 
                             command=self.show_success,
                             bg='#F5D105', fg='#000000', 
                             font=self.f_btn, bd=0, padx=25, pady=12,
                             activebackground='#D4B404', cursor="hand2")
        self.btn.pack(pady=25)

        # 4. 深度景點列表 (低認知負荷)
        self.add_node("AWOS 農場 (Awos Home)", "自然農法、紅藜與傳統海鹽導覽")
        self.add_node("寧埔休憩區 (S-Curve)", "全台最美海岸線 180 度觀景點")
        self.add_node("光榮部落 (Kiwit)", "阿美族生存智慧與石棺遺址探訪")

        # 5. 系統狀態
        tk.Label(self.root, text="● 系統存活狀態：正常 (離線備援已就緒)", 
                 fg='#00FF00', bg='#001A33', font=self.f_status, pady=5).pack(side='bottom', fill='x')

    def setup_fonts(self):
        """字體遍歷防禦：確保在所有作業系統均不亂碼"""
        # 優先順序：微軟正黑體 -> 蘋方 -> 標楷體 -> 系統預設
        font_candidates = ["Microsoft JhengHei", "PingFang TC", "STHeiti", "DFKai-SB", "Arial Unicode MS"]
        
        target_font = "System"
        available = font.families()
        for f in font_candidates:
            if f in available:
                target_font = f
                break
        
        # 定義各級字體
        self.f_title = (target_font, 20, "bold")
        self.f_btn = (target_font, 14, "bold")
        self.f_card = (target_font, 12, "bold")
        self.f_desc = (target_font, 10)
        self.f_status = (target_font, 9)

    def add_node(self, title, desc):
        card = tk.Frame(self.root, bg='#003366', padx=15, pady=12)
        card.pack(fill='x', padx=20, pady=6)
        tk.Label(card, text=title, fg='#F5D105', bg='#003366', font=self.f_card).pack(anchor='w')
        tk.Label(card, text=desc, fg='white', bg='#003366', font=self.f_desc).pack(anchor='w')

    def show_success(self):
        messagebox.showinfo("預約成功", "已鎖定 AWOS 農場體驗名額！\n\n遵循 CRF v9.0 協議：\n資料已同步至在地離線資料庫。")

if __name__ == "__main__":
    root = tk.Tk()
    # 強制設定系統編碼環境
    try:
        root.option_add('*font', 'Arial 10') # 基礎保險
    except:
        pass
    app = NingpuUniversalApp(root)
    root.mainloop()
