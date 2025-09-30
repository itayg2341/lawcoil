# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os.path import basename
from urllib.error import HTTPError
from urllib.request import urlopen

import io

from django.core.files import File
from django.db import migrations, models

LAWYERS = [
    {
        'language': 'he',
        'name': 'חיים רביה',
        'slug': 'haim-ravia',
        'email': 'HRavia@PearlCohen.com',
        'phone': '09-9728083',
        'short_description': '''
        <p>אחד מעורכי הדין הבולטים בישראל ובעולם בתחומי הסייבר ואבטחת המידע, על-פי הפרסום העולמי של Who's Who Legal לשנים 2010 - 2015. עו&quot;ד רביה צבר ניסיון ארוך שנים בייעוץ לחברות הפועלות בתחומי הטכנולוגיה - החל ממיזמים של איש אחד וכלה בחברות ענק בינלאומיות - בתחומים כדוגמת המשפט והאינטרנט, טכנולוגיות מידע, פרטיות ואבטחת מידע, זכויות יוצרים וקוד פתוח.</p>
        ''',
        'description': '''
        <p>&nbsp;שותף בכיר ב<a href="http://www.pczlaw.com">פרל כהן צדק לצר ברץ</a>. אחד מעורכי הדין המובילים בישראל ובעולם בתחומי הסייבר ואבטחת המידע, על-פי הפרסום העולמי של Who's Who Legal לשנים 2010 - 2015. בוגר הפקולטה למשפטים באוניברסיטת תל-אביב (1988) בעל תואר LL.B., חבר לשכת עורכי הדין בישראל (1990). ייסד בשנת 1993 את רביה ושות', עורכי דין, משרד שהיה לימים הראשון בישראל&nbsp;לעסוק&nbsp;בהבטים משפטיים של אינטרנט ומערכות מידע. ב-2013 הוענק לו&nbsp;אות הוקרה על חדשנות וחלוציות בתחום האינטרנט בישראל על-ידי לשכת מנתחי מערכות המידע. בשנת 2007 התמזג המשרד עם <a href="http://www.pczlaw.com">פרל כהן צדק לצר</a>. משמש כראש קבוצת האינטרנט, ה- IT וזכויות היוצרים במשרד הממוזג.<br />
<br />
יושב ראש ועדת מיחשוב הארצית בלשכת עורכי הדין (2007 - 2008), חבר נשיאות ועדת המחשוב בלשכת עוה&quot;ד (2000 - 2005) ונציגה לדיוני הכנסת בנושא חוק החתימה האלקטרונית. חבר המועצה הציבורית להגנת הפרטיות הפועלת ליד משרד המשפטים מכוח חוק הגנת הפרטיות, התשמ&quot;א - 1981. חבר צוות הבדיקה להסדרי רישום מאגרי המידע בישראל (2007). מרצה אורח בפקולטה למשפטים באוניברסיטת חיפה (&quot;ראיות ועבירות מחשב&quot; - 2002-2003). חבר הוועדה לגיבוש קוד אתי לפרסום מידע כלכלי באינטרנט בראשות פרופ' אסא כשר (רשות ניירות ערך). מוסמך בגישור. נוטריון.&nbsp;<br />
<br />
<br />
עו&quot;ד רביה עוסק בייעוץ המשפטי והייצוג בתחום דיני המחשבים, החתימה האלקטרונית, הקניין הרוחני והשימוש באינטרנט. לצד השירותים ללקוחות הקבוצה בתחום זה, עו&quot;ד רביה מפרסם מאז 1996 מדור בסוגיות אלה ב&quot;גלובס&quot; (<a href="/articles/">כ- 200 מאמרים נמצאים באתר law.co.il</a>), ומרצה בנושאים הללו בפני פורומים שונים (השתלמויות שופטים, האיגוד לאבטחת מידע, איגוד האינטרנט הישראלי ועוד).</p>
        ''',
        'profile_photo_url': 'https://pearlcohen.com/media/small_photos/DSC_9443_w.jpg',
        'large_photo_url': 'https://pearlcohen.com/media/photos/Haim%20Ravia_b.jpg',
        'order': 1,
    },
    {
        'language': 'he',
        'name': 'טל קפלן',
        'slug': 'tal-kaplan',
        'email': 'TKaplan@PearlCohen.com',
        'phone': '09-9728087',
        'short_description': '''
<p>        בוגר משפטים ומנהל עסקים בהצטיינות, המרכז הבינתחומי בהרצליה (2003), חבר לשכת עורכי הדין בישראל (2004)</p>
        ''',
        'description': '''
<p>  שותף בפרל כהן צדק לצר ברץ. בוגר משפטים ומנהל עסקים בהצטיינות, המרכז הבינתחומי בהרצליה (2003), חבר לשכת עורכי הדין בישראל (2004). מרכז את הטיפול בקבוצה ברישוי יצירות מוגנות לשימוש באינטרנט ובשמות מתחם (Domain Names).</p>
        ''',
        'profile_photo_url': 'https://pearlcohen.com/media/small_photos/DSC_0902_w.jpg',
        'large_photo_url': 'https://pearlcohen.com/media/photos/DSC_0902_w.jpg',
        'order': 2,
    },
    {
        'language': 'he',
        'name': 'דותן המר',
        'slug': 'dotan-hammer',
        'email': 'DHammer@PearlCohen.com',
        'phone': '09-9728242',
        'short_description': '''
<p>בוגר משפטים בהצטיינות, המרכז הבינתחומי הרצליה (2011) ומדעי המחשב בהצטיינות, האוניברסיטה הפתוחה (2002).&nbsp; חבר לשכת עורכי הדין בישראל (2012).</p>
        ''',
        'description': '''
<p>בוגר משפטים בהצטיינות, המרכז הבינתחומי הרצליה (2011) ומדעי המחשב בהצטיינות, האוניברסיטה הפתוחה (2002). חבר לשכת עורכי הדין בישראל (2012). עוסק בייעוץ משפטי בקשר עם הסכמי רישיון ותנאי שימוש לאתרים ולתוכנות, חתימות אלקטרוניות, זכויות יוצרים, קוד פתוח ונושאים נוספים בזיקה שבין עולם המשפט לעולם המחשבים והאינטרנט.<br />
<br />
השלים את לימודיו האקדמאים במדעי המחשב בגיל 19 ולאחר שירותו הצבאי עסק בפיתוח תוכנות והובלת פרויקטי טכנולוגיה בשירות המדינה. שימש בעבר כעוזר מחקר בתחום הקניין הרוחני במרכז הבינתחומי.</p>
        ''',
        'profile_photo_url': 'https://pearlcohen.com/media/small_photos/DSC_9598_w.jpg',
        'large_photo_url': 'https://pearlcohen.com/media/photos/DSC_9598_b.jpg',
        'order': 3,
    },
    {
        'language': 'en',
        'name': 'Haim Ravia',
        'slug': 'haim-ravia',
        'email': 'HRavia@PearlCohen.com',
        'phone': '+972-9-972-8083',
        'short_description': '''
<p>Graduate of the Tel Aviv University Law Faculty (1988), L.L.B., member of the Israel Bar Association (1990). Chair of the Praesidium of the IBA Computing Committee (2007-2008) and its representative to the Knesset sessions on Electronic Signature legislation. Notary &amp; accredited mediator.</p>
        ''',
        'description': '''
<p>Senior Partner at <a href="http://www.pczlaw.com">Pearl Cohen Zedek Latzer Baratz</a> and Chair of the Internet, Cyber &amp; Copyright group.</p>
<p>Selected by&nbsp;<a href="http://www.chambersandpartners.com/">Chambers &amp; Partners</a>&nbsp;as a Notable Practitioner.&nbsp;Graduate of the Tel Aviv University Law Faculty (1988), L.L.B., member of the Israel Bar Association (1990). Chair of the Praesidium of the IBA Computing Committee (2007-2008). Member of the Praesidium of the IBA Computing Committee (2000 &ndash; 2005) and its representative to the Knesset sessions on Electronic Signature legislation. Member of the Public Committee for the Protection of Privacy, acting under the auspices of the Ministry of Justice by virtue of the Protection of Privacy Law &ndash; 1981 (2001 &ndash; 2006). Member of the team re-examining regulations for the registration of databases in Israel (2005 - 2006). Visiting lecturer at the Haifa University Law Faculty (&quot;Evidence and Computer Crime&quot;, (2002-2003). Member of the committee established to formulate a Code of Ethics for transmitting financial information over the Internet, headed by Prof. Asa Kasher (Israel Securities Authority). Member of the Hi Tech International Law Association. Accredited Mediator.  Notary.</p>
<p>Adv. Ravia. deals in legal counseling and representation in the areas of computer &amp; Internet law, electronic signature, Copyright, Data Protection and Open Source Software. In addition to his work at the group, Adv. Ravia has been writing a column in Globes and The Israel Bar Association Magazine (1996 &ndash; 2005) on these issues, operates Israel's first legal website (www.law.co.il) and lectures on issues of his expertise.</p>
        ''',
        'profile_photo_url': 'https://pearlcohen.com/media/small_photos/DSC_9443_w.jpg',
        'large_photo_url': 'https://pearlcohen.com/media/photos/Haim%20Ravia_b.jpg',
        'order': 1,
    },
    {
        'language': 'en',
        'name': 'Tal Kaplan',
        'slug': 'tal-kaplan',
        'email': 'TKaplan@PearlCohen.com',
        'phone': '+972-9-972-8087',
        'short_description': '''
        <p>Graduate of the Law Faculty and the Business School, cum laude, Herzliya Interdisciplinary Center (2003), member of the Israel Bar Association (2004)</p>
        ''',
        'description': '''
<p>Graduate of the Law Faculty and the Business School, cum laude, Herzliya Interdisciplinary Center (2003), member fo the Israel Bar Association (2004). Heads the group's work on domain names. Married with&nbsp;two children.</p>
        ''',
        'profile_photo_url': 'https://pearlcohen.com/media/small_photos/DSC_0902_w.jpg',
        'large_photo_url': 'https://pearlcohen.com/media/photos/DSC_0902_w.jpg',
        'order': 2,
    },
    {
        'language': 'en',
        'name': 'Dotan Hammer',
        'slug': 'dotan-hammer',
        'email': 'DHammer@PearlCohen.com',
        'phone': '+972-9-972-8242',
        'short_description': '''
<p>Graduate of the Law Faculty , cum laude, Herzliya Interdisciplinary Center (2011). Graduate of Computer Sciense , cum laude, the Open University (2002). Member of the Israel Bar Association (2012).</p>
        ''',
        'description': '''
        <p>Dotan is a senior associate in the Internet, IT &amp; Copyright Group in Pearl Cohen&rsquo;s Herzliya office. Dotan's practices include software and website licenses and user agreements, digital (electronic) signatures, copyright issues, open source matters and other aspects of the law relating to computers, the Internet, and information technology.   Having completed his academic degree in computer science at the age of 19, later working as a software developer and a technological project leader in the public sector in Israel, Dotan now utilizes his technological background to focus on the interplay of law and technology and counsels clients in this novel domain of law. Prior to joining Pearl Cohen, Dotan also served as a legal research assistant to an IP law professor at the IDC.</p>
        ''',
        'profile_photo_url': 'https://pearlcohen.com/media/small_photos/DSC_9598_w.jpg',
        'large_photo_url': 'https://pearlcohen.com/media/photos/DSC_9598_b.jpg',
        'order': 3,
    },
]


def attach_image(field, url):
    """Downloads and stores the image for the feild"""
    try:
        response = urlopen(url)
        data = io.BytesIO(response.read())
        filename = basename(url)
        field.save(filename, File(data))
    except HTTPError:
        pass


def load_lawyers(apps, schema_editor):
    Lawyer = apps.get_model('lawyers', 'Lawyer')

    valid_fields = [f.name for f in Lawyer._meta.get_fields()]
    for lawyer in LAWYERS:
        just_model_fields = {k: lawyer[k] for k in valid_fields if k in lawyer}
        instance = Lawyer(**just_model_fields)

        attach_image(instance.profile_photo, lawyer['profile_photo_url'])
        attach_image(instance.large_photo, lawyer['large_photo_url'])

        instance.save()


def unload_lawyers(apps, schema_editor):
    Lawyer = apps.get_model('lawyers', 'Lawyer')
    slugs = set([x['slug'] for x in LAWYERS])
    Lawyer.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_lawyers, reverse_code=unload_lawyers)
   ]
