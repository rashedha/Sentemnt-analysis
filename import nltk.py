 ! pip install nltk

import nltk
nltk.download('punkt')
from textblob.classifiers import NaiveBayesClassifier

# هنا نضع الجمل الايجابية و السلبية لتدريب البرنامج على قراءة مشاعر الكلمات

train = [
('الجو رائع', 'pos'),
('الحديقة مناسبة للجلوس', 'pos'),
('السيارة سريعة', 'pos'),
('الشوكلاتة لذيذة', 'pos'),
("الايجار معقول", 'pos'),
("القهوة لذيذة", 'pos'),
("هذا المقهى جلساته مريحة", 'pos'),
("قصائد البدر جميلة", 'pos'),
("الشتاء فصل السعادة", 'pos'),
("العائلة مصدر السعادة", 'pos'),
("معالجة اللغات مادة جميلة", 'pos'),
("الشهادة الجامعية مصدر قوة", 'pos'),
("الاتحاد فريق قوي", 'pos'),
("صوت المنشد رائع", 'pos'),
("الاجواء في الجنوب صيفا رائعة ", 'pos'),
("دولتنا دولة قوية اقتصاديا ", 'pos'),
("السيارة سريعة ", 'pos'),
("جامعة الامام جامعة قوية", 'pos'),
("النخيل تبعث الحياة", 'pos'),
("قسم الحاسب يمتاز بجودة هيئة اعضاء التدريس", 'pos'),
("الزملاء متعاونين", 'pos'),
("الخطة الدراسية واضحة", 'pos'),
("الخدمات في الاحساء متوافرة بشكل جيد", 'pos'),
("المقاهي متوافرة بكثرة", 'pos'),
("المطاعم كثيرة و متنوعة ", 'pos'),
('الموقف سيء', 'neg'),
('المكان مزعج', 'neg'),
('النظافة معدومة', 'neg'),
('الأكل بارد', 'neg'),
('الفريق مو عارف يلعب','neg'),
('الارضية سيئة','neg'),
('الوقت غير كافي','neg'),
('الماء غير بارد','neg'),
('التوست مو مستوي','neg'),
('المسجل صوته ضعيف','neg'),
('العجلات غير صالحة','neg'),
('الصوت مو واضح','neg'),
('المكيف ما يبرد','neg'),
('الارضية مبتلة جدا ','neg'),
('المكان مزدحم ','neg'),
('اللابتوب يطيء ','neg'),
('هذا المحل غير مرتب','neg'),
('المكافئات تاخرت بالنزول','neg'),
('السرير غير مريح','neg'),
('الصيف بالشرقية رطوبة  ','neg'),
('الاحساء حارة بالصيف','neg'),
('كورونا اثر بشكل سلبي على العالم','neg'),
('صياح الاطفال مزعج','neg'),
('معدل البطالة مرتفع','neg'),
('شركات الشحن دائمة التأخير','neg'),
('المقاهي مزدحمة','neg')
]
#هنا نضع جمل الاختبار 
test = [
('مقهى رائع', 'pos'),
('الجو شديد البرودة ', 'neg'),
("القهوة لذيذة", 'pos'),
('الجودة مناسبة مقارنة بالسعر', 'pos'),
( 'المكان غير مبهج','neg'),
( 'المكان غير مبهج','neg'),
( ' لايستحق المشوار','neg'),
("المندي مضبوط",'pos'),
("صوت الاطفال عالي ",'neg'),
("النادي مرتب ", 'pos')
]


classifier = NaiveBayesClassifier(train) # استخدم المصنف classifier  لاختبار الجمل 
print(classifier.accuracy(train)) #حساب دقة جمل التدريب
print(classifier.accuracy(test)) #حساب دقة جمل الاختبار

for i in test:
  print(i[0],cl.classify(i[0]))

