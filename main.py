# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    information = """
    Việt Nam, quốc hiệu đầy đủ là Cộng hòa xã hội chủ nghĩa Việt Nam,[11] là một quốc gia nằm ở cực Đông của bán đảo Đông Dương thuộc khu vực Đông Nam Á, giáp với Lào, Campuchia, Trung Quốc, biển Đông và vịnh Thái Lan.

Lãnh thổ Việt Nam xuất hiện con người sinh sống từ thời đại đồ đá cũ, khởi đầu với các nhà nước Văn Lang, Âu Lạc. Âu Lạc bị nhà Triệu ở phương Bắc thôn tính vào đầu thế kỷ thứ 2 TCN sau đó là thời kỳ Bắc thuộc kéo dài hơn một thiên niên kỷ. Chế độ quân chủ độc lập được tái lập sau chiến thắng của Ngô Quyền trước nhà Nam Hán, mở đường cho các triều đại độc lập kế tục, nhiều lần chiến thắng trước các cuộc chiến tranh xâm lược từ phương Bắc đồng thời dần mở rộng về phía nam. Thời kỳ Bắc thuộc cuối cùng kết thúc sau chiến thắng trước nhà Minh của nghĩa quân Lam Sơn.

Đến thời cận đại, Việt Nam lần lượt trải qua các giai đoạn Pháp thuộc và Nhật thuộc. Sau khi đánh bại và buộc Nhật Bản đầu hàng, khối Đồng Minh tạo điều kiện cho Pháp thu hồi Liên bang Đông Dương. Kết thúc Thế chiến II, các nước Đồng Minh tiến vào Việt Nam giải giáp quân đội Nhật, bao gồm Anh Quốc, Pháp (ở miền Nam) và Trung Hoa Dân Quốc (ở miền Bắc). Nhà nước Việt Nam Dân chủ Cộng hòa do Việt Minh lãnh đạo ra đời khi Hồ Chí Minh tuyên bố độc lập vào ngày 2 tháng 9 năm 1945 sau thành công của Cách mạng Tháng Tám. Việt Minh chiến thắng Liên hiệp Pháp, bao gồm Quốc gia Việt Nam, trong Chiến tranh Đông Dương lần thứ nhất. Sự kiện này dẫn tới Hiệp định Genève 1954 được ký kết và Việt Nam bị chia cắt thành hai vùng tập kết quân sự, lấy ranh giới là vĩ tuyến 17. Việt Nam Dân chủ Cộng hòa kiểm soát phần phía bắc còn phía nam do Việt Nam Cộng hòa (nhà nước kế tục Quốc gia Việt Nam) kiểm soát và được Hoa Kỳ hậu thuẫn. Xung đột về thống nhất lãnh thổ đã dẫn tới Chiến tranh Việt Nam với sự can thiệp của nhiều nước và kết thúc với chiến thắng của Việt Nam Dân chủ Cộng hòa, Mặt trận Dân tộc Giải phóng miền Nam Việt Nam cùng sự sụp đổ của Việt Nam Cộng hòa vào năm 1975. Chủ quyền phần phía Nam được chính quyền Cộng hòa miền Nam Việt Nam (do Mặt trận Dân tộc Giải phóng miền Nam Việt Nam thành lập) giành quyền kiểm soát. Năm 1976, Việt Nam Dân chủ Cộng hòa và Cộng hòa miền Nam Việt Nam thống nhất thành Cộng hòa xã hội chủ nghĩa Việt Nam.

Một nền kinh tế kế hoạch hóa không hiệu quả, lệnh cấm vận thương mại của phương Tây, cùng chiến tranh với Campuchia và Trung Quốc đã khiến tình trạng khó khăn hơn. Năm 1986, Đảng Cộng sản Việt Nam khởi xướng các cải cách kinh tế và chính trị tương tự cải cách kinh tế của Trung Quốc, đưa đất nước chuyển đổi sang nền kinh tế thị trường định hướng xã hội chủ nghĩa. Những cải cách này tạo điều kiện cho Việt Nam tái hội nhập vào nền kinh tế thế giới và chính trị quốc tế. Việt Nam là một nước đang phát triển với nền kinh tế có thu nhập trung bình cao.[12] Giới bất đồng chính kiến Việt Nam và một số nước phương Tây chỉ trích Việt Nam tồn tại tình trạng tham nhũng ở mức cao, sự kiểm duyệt, các vấn đề môi trường và hồ sơ nhân quyền yếu kém. Việt Nam là thành viên của nhiều tổ chức quốc tế và liên chính phủ, bao gồm ASEAN, APEC, Phong trào Không liên kết, OIF, và WTO. Việt Nam đã hai lần đảm nhiệm cương vị ủy viên Hội đồng Bảo an Liên Hợp Quốc.

"""

    summary_template = """
    given the information {information} I want you to create:
    1. A summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})

    print(response.content)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
