from getRequest import *
import streamlit as st
import hydralit_components as hc
import webbrowser

menu_data = [
    {'icon': "🌏", 'label': "Tam Zamanlı Veri Akışı"},
    {'icon': "🔎", 'label': "Road Map"},
    {'icon': "🔎", 'label': "Poisson Dağılımı ve Deprem Olasılığı"},
    {'icon': "🔎", 'label': "Tüm Depremlerin Harita Gösterimi"},
]

over_theme = {'txc_inactive': '#FFFFFF',
              'menu_background': '#55496b', 'txc_active': '#0f0f0f', 'option_active': '#b4d1d0', 'font-weight': 'bold'}

menu_id = hc.nav_bar(
    menu_definition=menu_data, home_name='Ana Sayfa | Bilgilendirme | Kullanım', override_theme=over_theme)

st.info("AFAD Ve Kandilli Rasathanesinden Alınan Verileri Derleyip Harmanlayıp Tek Bir Yerde Bakmanız İçin Kodlanmış Bir Uygulamadır!")


def app():
    st.title("Deprem Planları, Neler Yapılmalı?")

    Text = """
    1. Risklerini bilin ve deprem anına yönelik plan yapın

    Deprem riski taşıyan bir bölgede yaşayıp yaşamadığınızı, binanızın depreme dayanıklılığını ölçtürüp öğrenmeniz ilk adımdır. Deprem anında, yaşadığınız yerde nereye gideceğiniz konusunda önceden düşünmeniz gerekir. Deprem sarsıntısı korku duygusunu yoğun olarak açığa çıkardığı için deprem anında birçok planın gerçekleşmediği görülse de önceden hazırlık yapmak deprem anında daha soğukkanlı olmaya yardımcı olur. Bu sebeple hazırlıklarınızı tüm aile üyeleriyle birlikte yapmanız, küçük çocuklarınız varsa eşinizle önceden belirlediğiniz plana çocuklarınızı eğlenceli bir biçimde ve bir oyunun içinde, kaygı uyandırmayacak şekilde katmanız önerilir.


    Aile üyeleri evde, iş yerlerinde ve okullarında, her odada deprem esnasında duracakları güvenli yeri belirlemelidir. Ailedeki yetişkinler olarak pencere yakınları, dış kapılar, dış duvarlar ve düşebilecek şeyler gibi güvenli olmayan alanları, ayrıca çök-kapan-tutun hareketini yapabilecekleri güvenli yerleri önceden belirleyin ve bunları çocuklarınıza bildirin. Mobilya, su ısıtıcısı gibi eşyaları ve kayabilecek veya düşebilecek şeyleri önceden sabitleyin. Gaz ve su vanalarının, elektrik sigortasının nasıl kapanacağını öğrenin. Hasarlı elektrik kablolarını ve gaz sızıntısı yapma riski olabilecek tesisat bağlantılarını kontrol edin, gerekirse onarın. Aile üyelerine, deprem sarsıntısı durana kadar içeride kalmaları gerektiğini hatırlatın. Deprem bittikten sonra binadan dışarıya çıkış için en güvenli yolu ve acil toplanma alanını önceden belirlemiş olun.


    Aile üyeleri dışarıda olduğu zaman depremin yaşanması halinde, cep telefonu hatlarında iletişim kesintiye uğrayabileceğinden dolayı bir buluşma yerini önceden belirleyebilirsiniz. Bu alan ulaşabileceklerinden uzakta bir yer de kalırsa aile üyelerinin eğer güvenli ise bulundukları yerde kalmalarını, binalardan, kablolardan veya düşebilecek nesnelerden uzak ve güvenli bir yerde durmaları konusunda önceden hemfikir olun. Ailece bir depreme hazırlık toplantısı yapın ve bu toplantıda çök-kapan-tutun hareketinin tatbikatını yapın.


    2. İletişim için plan yapın

    Aile üyelerinin deprem sonrasında birbirinden haberdar olması için bir aile iletişim planı yapın. Aile üyeleri, kolayca erişilebilecek önemli iletişim bilgilerine sahip olmalı ve birbirlerinden ayrıldıklarında kiminle iletişim kurabileceklerini bilmelidir. Bebek bakıcısı, komşu, yakın akraba gibi kişileri plandan haberdar edin. İletişim numaralarını, irtibat kurulabilecek kurumların telefon numaralarını bu kişilerle paylaşın. Çocukların evde veya okulda ne yapacaklarını bildiklerinden emin olun. Okula ulaşamamanız halinde ne yapılması gerektiği konusunda okul yetkilileri ile mutabık kalın ve çocuğunuzu da bilgilendirin. Küçük bir fikir; Okulöncesi dönemde olan küçük çocuğunuz varsa, evinizdeki deprem çantası içine konabilecek resimli bir not kâğıdı bulundurabilir, çocuğunuza bakım veren kişilerin bu kâğıdı ona göstermesini sağlayabilir, böylece sizinle tekrar temas kurana kadar rahat hissetmesi için çocuğunuza yardımcı olabilirsiniz.


    3. İhtiyaçlar için plan yapın

    Deprem öncesinde deprem çantası hazırlığı, eşyaların sabitlenmesi ve olası risklerin belirlenmesi, ayrıca deprem anına yönelik eylem planı yapmanın yanı sıra aile üyelerinin ihtiyaçları için de ayrıca planlar yapın. Sağlık durumu dolayısıyla düzenli ilaç kullanan aile bireyleri, özel gereksinimi olan bireyler için hazırlıkları yapın ve yakınlarınızı da haberdar edin. İlk fırsatta ilkyardım eğitimleri alın. Çocukların ihtiyaçları için de ayrıca plan yapın. Bu ihtiyaçların içinde, çocuklara depremi anlatmak ve onları depreme hazırlamak da bulunur. Çocukları deprem hakkında basit terimlerle gerçekçi bilgiler ile önceden bilgilendirin. Okulöncesi çocuğunuz için oyunlar aracılığıyla depremin ne olduğunu kısa, basit bilgilerle anlatabilirsiniz. Olası durumlardan bahsetmeniz ve yetişkinler olarak onun güvende olması için gerekli tedbirleri aldığınızı belirtmeniz onun güvende hissetmesine yardımcı olur. Kaygı uyandırmayacak ölçüde gerçekçi bilgiler vermeye gayret edin.


    Çocuğunuzun bakıcısı varsa, onun da deprem hazırlıklarına dahil olmasını sağlayın ve çocuğunuza verilecek bilgiler konusunda gereklilikleri, ayrıca sınırları bildirin. Çocuğunuzda kaygı uyandıracak ifadeler veya detay bilgileri kullanmaması, çocuğunuzun güvenlik hissini koruyacak davranışlarda bulunması konusunda bakıcınızı yönlendirin. Yatılı bakıcınız bulunuyorsa, onun da bir kişisel deprem çantasının bulunması konusunda kendisini teşvik edin ve depremle ilgili tüm tatbikat, bilgilendirme gibi hazırlıklara onu da dahil edin. Siz evde bulunmadığınız zaman deprem olması durumunda neler yapması gerektiği konusunda bakıcınıza bilgi verin. Tüm bunların hem aileniz hem de onun can güvenliği için gerektiği konusunda açıklayıcı olun.


    Deprem çantası hazırlayın

    Aileniz için bir deprem çantası hazırlayın. Çocuklarınızın da kendi kitlerini hazırlamaları, onların kontrol duygusunu korumaları açısından faydalı olacaktır. Okul öncesi dönemdeki çocuklar için boya kalemleri, su matarası gibi eşyalarının aynılarını barındıran bir deprem çantasını birlikte hazırlamanız onların da konuya rahatça dahil olmalarına yardımcı olur.


    Ailenin deprem çantasında yer alması gereken ilaç gibi malzemelerin son kullanma tarihlerini düzenli aralıklarla kontrol etmeyi unutmayın.
    """

    st.markdown("# Depreme Hazırlık")
    st.write(Text)


if(st.button("Sayfaya Erişim Yok Deprem Bilgilerini Okumak İçin Butona Basınız!")):
    app()
