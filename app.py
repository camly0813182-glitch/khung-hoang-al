import streamlit as st
import google.generativeai as genai

# 1. CẤU HÌNH API (Giữ nguyên Key của bạn)
genai.configure(api_key="AIzaSyAPr01OtkLHaNMXYc3nYRRbBuePtFE03OQ")

# 2. THIẾT LẬP GIAO DIỆN
st.set_page_config(page_title="Hệ thống Khủng hoảng AI", page_icon="🤖")

# 3. SIDEBAR CÀI ĐẶT
with st.sidebar:
    st.title("⚙️ Cấu hình")
    tinh_huong = st.selectbox("🎯 Tình huống:", ["Sản phẩm lỗi", "Nhân viên thô lỗ", "Dịch vụ chậm"])
    muc_do = st.select_slider("🔥 Mức độ giận dữ:", options=["Thấp", "Vừa", "Cao", "Cực đoan"])
    if st.button("🗑️ Xóa hội thoại"):
        st.session_state.messages = []
        st.rerun()

# 4. KHÔNG GIAN CHAT
st.title("🤖 Crisis Simulation AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Bạn sẽ giải quyết thế nào?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # 5. XỬ LÝ AI THÔNG MINH (TỰ ĐỘNG CHỌN MODEL)
    with st.spinner("Khách hàng đang soạn tin..."):
        try:
            # Ưu tiên dùng gemini-1.5-flash vì nó nhanh và mới nhất
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            huong_dan = f"Bạn là khách hàng VN đang {muc_do} giận dữ vì {tinh_huong}. Trả lời đanh đá, ngắn gọn câu này: {prompt}"
            response = model.generate_content(huong_dan)
            ai_reply = response.text
            
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
            with st.chat_message("assistant"):
                st.write(ai_reply)
                
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}. Vui lòng kiểm tra lại API Key hoặc Reboot app.")