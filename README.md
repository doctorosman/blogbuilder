# Blog Builder Python Modülü
Bu modül sayesinde Python dili ile basit statik bloglar oluşturabileceksiniz.

## Kullanımı
Öncelikle sağ üstteki download bölümünden repoyu indirin. themes klasörü içerisinde kullanacağınız tema dışındaki diğer tüm temaları silin. Ana dizine gelerek bir python dosyası oluşturun.

```python
import blogbuilder as bb

bb.config('simple-blog', 'Blogunuzun İsmi', 'HTML Title\'ı', 'Profil Fotoğrafınızın Yolu (Url de olabilir)', 'Sayfanın en altında görünecek yazı')
bb.post('yazinizin-turkce-karakter-kullanmadan-yazilacak-yol-ismi', 'Yazınızın Başlığı', 'Yazınızın Fotoğrafının Yolu (Url de olabilir)', 'Yazınızın özeti', 'Yazınızın içeriği (html taglerini kullanabilirsiniz)')
# diğer postlarınız da buraya gelecek
bb.build()
```

İçini yazdıktan sonra python dosyanızı çalıştırın. Bazı sistemlerde yönetici olarak çalıştırmanız da gerekebilir.

## Katkı Sağlamak
Projeyi forkleyerek kod kısmına katkı sağlayabilirsiniz. Tema olarak katkı sağlamak için yine projeyi forkleyerek html dosyalarını "simple-blog" temasındaki gibi yazabilirsiniz.