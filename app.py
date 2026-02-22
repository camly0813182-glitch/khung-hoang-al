    # --- THAY THẾ ĐOẠN PHẢN HỒI CŨ BẰNG ĐOẠN NÀY ---
    import random
    
    # Danh sách các phản hồi khác nhau tùy theo mức độ giận dữ
    if muc_do == "Thấp":
        phan_hoi_list = [
            "Tôi tạm chấp nhận lời giải thích này, nhưng đừng để xảy ra lần nữa!",
            "Vậy phương án bồi thường cụ thể của các người là gì?",
            "Tôi cần một lời cam kết bằng văn bản."
        ]
    elif muc_do == "Trung bình":
        phan_hoi_list = [
            "Các người nói câu này bao nhiêu lần rồi? Tôi muốn giải quyết ngay!",
            "Thái độ phục vụ của bên bạn thật sự có vấn đề.",
            "Tôi không hài lòng, tôi sẽ cân nhắc việc ngừng sử dụng dịch vụ."
        ]
    else: # Mức Cao hoặc Cực đoan
        phan_hoi_list = [
            "ĐỪNG CÓ NÓI LÝ LẼ VỚI TÔI! Tôi sẽ đăng chuyện này lên hội nhóm 1 triệu thành viên!",
            "Tôi không cần xin lỗi, tôi muốn gặp quản lý của bạn NGAY LẬP TỨC!",
            "Các người đang coi thường khách hàng sao? Tôi sẽ báo công an và truyền thông!",
            "Quá sức chịu đựng rồi! Đợi thư luật sư của tôi đi!"
        ]
    
    # Chọn ngẫu nhiên một câu trong danh sách để trả lời
    rely = random.choice(phan_hoi_list)
    
    st.session_state.messages.append({"role": "assistant", "content": rely})
    with st.chat_message("assistant"):
        st.write(rely)
