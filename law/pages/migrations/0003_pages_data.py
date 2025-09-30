# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

PAGES = [
    {
        'language': 'he',
        'title': 'תנאי שימוש',
        'slug': 'terms',
        'content': '''
        <p>ברוכים הבאים ל- law.co.il, אתר-סף ('פורטל') למידע בנושאי משפט, מחשבים ואינטרנט. השימוש ב- law.co.il ובכל המדורים המשולבים בו (&quot;האתר&quot; או   &quot;law.co.il&quot;) כפוף לתנאי שימוש אלה. קרא אותם בקפידה, שכן השימוש באתר מעיד על הסכמתך להם. תנאי שימוש אלה מנוסחים בלשון זכר לצרכי נוחות בלבד, אולם   הם מתייחסים, כמובן, גם לנשים.</p>
<p class="subtitle">על האתר</p>
<p>law.co.il הוא האתר המשפטי הראשון באינטרנט הישראלי. הוא פעיל מאז מרץ 1996. הבעלים והמנהל של האתר הוא עו&quot;ד חיים רביה (&quot;מנהל האתר&quot;). ככל שיש באתר דיעות, הן דעותיו הפרטיות בלבד ואינן דעותיו של כל משרד עורכי דין שבו הוא שותף או דיעות לקוחותיו. שאלות   הנוגעות לאתר ניתן להפנות למנהל האתר באמצעות טופס משוב זה.</p>
<p>לתשומת לב: השימוש באתר אינו כרוך בתשלום, אבל אחריות מנהל האתר מוגבלת כאמור במפורש בתנאי שימוש אלה. לפרטים ראה, בין השאר, את הסעיף   &quot;העדר אחריות&quot; להלן.</p>
<p class="subtitle">קישורים באתר</p>
<p>ב- law.co.il תמצא קישורים והפניות לאתרים משפטיים ולמידע משפטי ברשת האינטרנט. זכור: אתרי האינטרנט והמידע הללו אינם מתפרסמים על ידי מנהל האתר   והוא אינו שולט או מפקח עליהם. הקישור לאתרים ולמידע משפטי אינו מעיד שהם נבדקו ונמצאו מהימנים, עדכניים, מלאים או מדויקים. זאת ועוד: אתרים ומידע   משתנים ומתעדכנים בקצב מסחרר - גם בגלל חידושי המשפט (בפרט בתחומו הדינמי של law.co.il) וגם בגלל השינויים התכופים המאפיינים את רשת האינטרנט. מה   שהיה עדכני ושלם היום, ייתכן שכבר יהיה חסר או שגוי מיסודו מחר.</p>
<p>אינדקס האתרים המקוון במדור &quot;קישורים משפטיים&quot; נערך על פי שיקול הדעת הסובייקטיבי של מנהל האתר. סדר האתרים המופיעים באינדקס אינו מעיד על טיבם או   חשיבותם של האתרים. למרות שמנהל האתר עושה מאמצים להבטיח שתאור האתרים באינדקס יהיה ממצה, הוא אינו יכול להבטיח כי תאור זה הנו הנכון והעדכני   ביותר.</p>
<p>מנהל האתר אינו מתחייב שכל הקישורים באתר יהיו תקינים ויובילו אותך לאתרי אינטרנט פעילים. מנהל האתר רשאי לסלק מאתר קישורים שנכללו בו בעבר, או   להימנע מהוספת קישורים חדשים - הכל, לפי שיקול דעתו המוחלט. העובדה שתמצא ב- law.co.il קישור לאתר מסוים אינה ערובה לכך שקישור זה לא יבוטל או   ישתנה.</p>
<p class="subtitle">מידע חדשותי ומאמרים</p>
<p>ב- law.co.il תמצא מאמרים וידיעות חדשותיות בסוגיות משפטיות הנוגעות לתחומי המשפט, המיחשוב והאינטרנט. המאמרים פורסמו ברובם לראשונה במדור   &quot;משפט באינטרנט&quot; בעיתון 'גלובס' ובבטאון לשכת עורכי הדין. הם מבטאים אך ורק את דעת הכותב, ואינם מתיימרים להיות שלמים, מקיפים, מלאים או עדכניים. אין   לסמוך על האמור במאמרים כעצה משפטית.</p>
<p>הידיעות החדשותיות המתפרסמות באתר אינן נוגעות רק לאינטרנט. הן עוסקות גם במחשבים, בחתימה אלקטרונית, בתוכנה חופשית, בתקשורת ובעוד נושאים   שבהם עוסק עו&quot;ד רביה (מהזווית המשפטית כמובן). מנהל האתר לא מתיימר להביא באתר את &quot;כל החדשות&quot; או את החדשות הכי חשובות, אלא רק את מה שמעניין אותו   ומגיע לידיעתו במסגרת עבודתו השוטפת. מנהל האתר משתדל לעדכן את המדור באופן שוטף, אבל לא תמיד הדבר יסתייע . בכל ידיעה ייעשה מאמץ להפנות למקורה,   והידיעה מדויקת רק במידה שהמקור מדויק. אם מנהל האתר הביע אגב כך את דעתו, המדובר תמיד בדעתו-שלו בלבד, אבל אין לראותה כחוות דעת משפטית או כדעת   לקוחותיו, משרדו או שותפיו למשרד.</p>
<p>חובה לזכור: לבעיות משפטיות תשובות שונות התלויות בדקויותיו של כל מקרה ומקרה. לא רק זה, אלא שהמאמרים והידיעות באתר פורסמו בחלקם לפני שנים   ארוכות (החל מ- 1997). ביחד עם כל מאמר וכל ידיעה, מופיע בבירור תאריך פרסומם המקורי. מה שהיה נכון לשעתו, שוב אינו עדכני בחלוף השנים. המשפט   והטכנולוגיה משתנים. תשובות שהיו תקפות בעבר שוב אינן עונות על דרישות ההווה. לפיכך, בעת שמתעוררת בעיה, הנזכרת במאמרים ובידיעות החדשותיות שבאתר,   יש להיוועץ בעורך דין והאמור ב- law.co.il איננו בשום פנים ואופן תחליף להיוועצות כזאת.</p>
<p class="subtitle">טפסים משפטיים</p>
<p>ב- law.co.il תמצא מדור של טפסים משפטיים. מילוי טפסים ובחירתם היא מלאכה הדורשת מיומנות מקצועית. יש להותירה בידי עורכי דין או לכל הפחות למסור   את הטופס לבדיקת עורך-דין לפני הגשתו לרשויות. יש לזכור - הפרטים בטופס יכולים לקבוע את זכויות הממלא!</p>
<p>טפסים מתעדכנים, משתנים ומוחלפים מעת לעת. מנהל האתר אינם יכולים לערוב לכך שהטפסים המופיעים כאן יהיו בכל עת העדכניים והנכונים. יש אפוא לבדוק   לפני השימוש בכל טופס כי הוא אמנם בתוקפו. במידה ומצאת שאחד הטפסים אינו עדכני עוד, נא הודע לנו באמצעות טופס המשוב באתר זה.</p>
<p>הטפסים נועדו לשימוש אישי בלבד או לשימוש שוטף במשרדי עורכי דין. אין לעשות בהם כל שימוש מסחרי או לצורך של הפקת רווח בלא לקבל את הסכמת מנהל   האתר בכתב ומראש. הבחירה באחד או יותר מן הטפסים המופיעים באתר, שמירתם במחשב המשתמש או השימוש בהם מעידים על הסכמה לאמור בתנאי שימוש אלה. אם   אינך מסכים להם, הימנע מהורדת הטפסים, שמירתם או השימוש בהם.</p>
<p class="subtitle">רשימות דיוור</p>
<p>חלק מהמידע ב- law.co.il מופץ באמצעות הודעות דואר אלקטרוני הנשלחות מעת לעת, בתדירות שיקבע מנהל האתר, למי שביקשו לקבלן. כדי להיות מנוי על   שירות זה, עליך לבקש זאת במפורש ולהירשם לשירות. במסגרת ההרשמה תתבקש למסור למנהל האתר את כתובת הדואר האלקטרוני שלך. הנך מתבקש לנהוג בקפידה   במסירת הפרטים ולמסור פרטים נכונים בלבד. מנהל האתר ישתמש במידע שתמסור על-פי מדיניות הפרטיות ב- law.co.il. בכל עת תוכל לחדול מקבלת הדואר   האלקטרוני באמצעות בקשה למנהל האתר.<br />
מנהל האתר רשאי להחליט, לפי שיקול דעתו המוחלט, שלא לספק את השירות למי מהנרשמים לו או לחדול מכל סיבה שהיא מאספקתו, בין אם למשתמש מסוים ובין אם   בדרך כלל.</p>
<p class="subtitle">RSS Feeds</p>
<p>חלק מהמידע ב- law.co.il מופץ באמצעות RSS Feeds. אין לשלב פרסומות ב-Feed או לשנותו בשום צורה ודרך בלא קבלת הסכמה ממנהל האתר בכתב ומראש.   מנהל האתר שומר על זכותו לדרוש מכל מי ששילב Feed באתר אינטרנט, בתוכנה או בשירות מקוון אחר, לחדול מכך בכל עת. מנהל האתר אינו חייב לנמק את דרישתו   ומי ששילב Feed כאמור מתחייב לפעול לפיה לאלתר.</p>
<p class="subtitle">פרטיות</p>
<p>מנהל האתר מכבד את פרטיות המשתמשים באתר. מדיניות הפרטיות העדכנית של האתר נמצאת בכל עת כאן, והיא מהווה חלק בלתי נפרד מתנאי שימוש אלה. הואיל   ומדיניות הפרטיות יכולה להשתנות מדי פעם, מומלץ שתחזור ותקרא אותה מדי פעם.</p>
<p class="subtitle">העדר אחריות</p>
<p>המידע והשירותים באתר ניתנים לשימוש כמות שהם (AS IS). לא ניתן להתאימם לצרכיו של כל אדם ואדם. לא תהיה לך כל טענה, תביעה או דרישה כלפי מנהל   האתר בגין המידע והשירותים המוצעים באתר או באמצעותו, דיוקם, מהימנותם, שלמותם, עדכניותם או תדירות פרסומם. השימוש וההסתמכות על המידע באתר ייעשה   אפוא על אחריותך הבלעדית והמלאה.</p>
<p>מנהל האתר לא ישא בשום פנים ואופן באחריות למידע המשפטי ולאתרים שאליהם מקשר law.co.il, לרבות שלמותו, מהימנותו, דיוקו או עדכניותו של כל אתר   ומידע כזה. כל המסתמך על אתרים משפטיים ומידע משפטי שקושרו מתוך law.co.il, עושה זאת על אחריותו בלבד.</p>
<p>אין להסתמך על מאמר או ידיעה חדשותית באתר זה כאילו היו עצה משפטית. חובה להיוועץ בעורך-דין לפני כל הסתמכות כזו. מנהל האתר לא ישא באחריות לכל   תוצאה שתנבע, במישרין או בעקיפין, מהסתמכות על מידע שהתפרסם באתר בלא היוועצות משפטית עם עורך-דין מיומן בתחום.</p>
<p>מנהל האתר לא ישא באחריות כלשהי לכל תוצאה, ישירה או עקיפה, שתנבע מהטפסים הנמצאים בו. השימוש בטפסים הינו על אחריות המשתמש בלבד.</p>
<p>מנהל האתר אינו מתחייב שפעולת האתר לא תופרע או תתנהל בלא הפסקות, בבטחה ובלא טעויות, קלקולים, תקלות או כשלים - והכל, בחומרה, בתוכנה, בקווי   ובמערכות תקשורת, אצל מנהל האתר או אצל מי מספקי השירותים לאתר.</p>
<p>מנהל האתר לא ישא בכל אחריות לחשיפת פרטים שנמסרו לאתר במקרה של חדירה שלא כדין למערכות המחשב של האתר.</p>
<p>מנהל האתר אינו נושא באחריות לתוכנם של אתרים המקושרים מ- law.co.il. בכלל זה מנהל האתר לא נושא באחריות למידע המתפרסם באתרים הנ&quot;ל לרבות   שלמותו, דיוקו, עדכניותו ונכונותו או כל פרט אחר הקשור עמו. מנהל האתר לא אחראי לכל נזק ישיר או עקיף, כספי או אחר, שייגרם כתוצאה משימוש או הסתמכות על   אתרים אלה.</p>
<p class="subtitle">קנין רוחני</p>
<p>כל זכויות היוצרים והקניין הרוחני באתר - לרבות במאמרים, בידיעות, בתבנית הטפסים או במידע טקסטואלי אחר מכל מין וסוג באתר, בעיצוב האתר ובכל תוכנה,   יישום, קוד מחשב, קובץ גרפי וכל תוכן אחר הכלולים בו - הינן של מנהל האתר בלבד. אין להעתיק, להפיץ, להציג בפומבי, לתרגם או למסור לצד שלישי כל חלק מן   הנ&quot;ל בלא קבלת הסכמתו המפורשת של מנהל האתר בכתב ומראש.</p>
<p>law.co.il הינו סימן מסחרי רשום של עו&quot;ד חיים רביה. האתר פועל גם באמצעות שמות-מתחם אחרים, כדוגמת Cyberlaw.co.il, it-law.co.il ואחרים. אין   להשתמש בשמות המתחם של האתר, בשם &quot;רביה&quot; או בסימן המסחר law.co.il בלא קבלת הסכמתו המפורשת של מנהל האתר בכתב ומראש.</p>
<p>באתר יכולים להימצא תכנים המתפרסמים על-פי הסכם בין מנהל האתר לבין צדדים שלישי כלשהם. זכויות היוצרים בתכנים אלה שייכות לצד השלישי שהרשה לאתר   להשתמש בהן. אין להעתיק, לשכפל, להפיץ, לשווק או למסור לציבור תכנים אלה או כל חלק מהם בלא קבלת הסכמה מפורשת מראש ובכתב מבעל הזכויות בהם.</p>
<p class="subtitle">השימוש באתר</p>
<p>אתר מיועד לשימוש אישי ופרטי בלבד. אין לעשות כל שימוש מסחרי בנתונם ובפרטים האחרים המתפרסמים באתר. אין להשתמש בנתונים כלשהם המתפרסמים   באתר לצורך הצגתם באתר אינטרנט או בשירות אחר כלשהו, בלא קבלת הסכמה של מנהל האתר בכתב ומראש, ובכפוף לתנאי אותה הסכמה (אם תינתן). בכלל זה נאסר   לאגור מידע ותכנים שהתפרסמו באתר באמצעות תוכנות מסוג (Crawlers, Robots וכד') או להפיץ מידע ותכנים כאלה ברבים באופן מסחרי או במסגרת מסחרית.</p>
<p>אין להציג את האתר בתוך מסגרת (Frame), גלויה או סמויה.</p>
<p>אין לקשר לעמודים המצויים בתוך האתר (&quot;קישור עמוק&quot;), אלא בתנאי שהקישור ייעשה לעמוד Web מלא, שיוצג בפני המשתמש ממחשבי אתר בלא כל התערבות   בעיצובו, בתוכנו או בפעולתו. בנוסף מותנה הקישור העמוק בכך שכתובתו המדויקת של העמוד מן האתר תופיע במקום הרגיל המיועד לכך בתוכנה המשמשת לעיון   באתר.</p>
<p>אין לקשר לרכיבים בודדים באתר - כדוגמת קישור ישיר לתמונות או למסמכים המצויים באתר, להבדיל מקישור לעמוד המלא שבו הם נמצאים.</p>
<p>אין להציג את האתר בעיצוב או מימשק גרפי שונים מאלה שקבע לו מנהל האתר, אלא בכפוף לקבלת הסכמתם לכך מראש ובכתב.</p>
<p>אין להציג את אתר באמצעות מערכות טכנולוגיות כלשהן באופן הגורע מן התכנים המצויים בו.</p>
<p class="subtitle">שינויים באתר</p>
<p>מנהל האתר רשאי, על פי שיקול דעתו הבלעדי וללא כל הודעה מוקדמת, למנוע ממך את השימוש באתר; למנוע גישה לאתר, כולו או חלקו; לבטל את הרשמתך   לשירותים באתר או להסיר או למחוק כל מידע או תוכן שהתפרסם באתר. בפרט, מנהל האתר יעשו זאת בכל מקרה של הפרת תנאים אלה ו בכל מקרה של מעשה או מחדל   הפוגע או העלול לפגוע בשירותים הניתנים באתר, במשתמשיו, במנהל האתר או במי מטעמו. הוראות סעיף זה מוסיפות על זכויות מנהל האתר על פי כל דין ועל-פי   הוראות אחרות בתנאי שימוש אלה.</p>
<p>מנהל האתר יוכל לשנות מעת לעת את מבנה אתר, מראה האתר, היקפם וזמינותם של השירותים הניתנים בו וכל היבט אחר הכרוך בהם - והכל, בלא צורך להודיע   לך על כך מראש. שינויים כאלה יבוצעו, בין השאר, בהתחשב באופי הדינמי של האינטרנט ובשינויים הטכנולוגיים והאחרים המתרחשים בה. מטבעם, שינויים מסוג זה   עלולים להיות כרוכים בתקלות או לעורר בתחילה אי-נוחות וכיו&quot;ב. לא תהיה לך כל טענה, תביעה ו/או דרישה כלפי מנהל האתר בגין ביצוע שינויים כאמור או תקלות   שיתרחשו אגב ביצועם.</p>
<p class="subtitle">הפסקת פעילות האתר</p>
<p>מנהל האתר רשאי לחדול מהפעלתו בכל עת, בלא הודעה מוקדמת, באופן קבוע או לתקופה קצובה.</p>
<p class="subtitle">שיפוי</p>
<p>הנך מתחייב לשפות את מנהל האתר, משרדו, עובדיו, מנהליו או מי מטעמו בגין כל נזק, הפסד, אבדן-רווח, תשלום או הוצאה שייגרמו להם - ובכלל זה שכ&quot;ט עו&quot;ד   והוצאות משפט - עקב הפרת תנאי שימוש אלה.</p>
<p class="subtitle">שינוי תנאי השימוש</p>
<p>מנהל האתר רשאי לשנות מעת לעת את תנאי השימוש באתר, בלא צורך בהודעה מוקדמת. בכל עת תוכל לעיין בתנאי השימוש העדכניים באמצעות לחיצה על   הקישור המתאים המופיע בעמודי האתר.</p>
<p class="subtitle">דין וסמכות שיפוט</p>
<p>על תנאים אלה יחולו אך ורק דיני מדינת ישראל. כל מחלוקת שתתגלה בין הצדדים לרבות מחלוקת בקשר עם השימוש באתר או בקשר עם תנאי שימוש אלה תהיה   נתונה לסמכות השיפוט הבלעדית של בית המשפט המוסמך עניינית במחוז תל-אביב בישראל.</p>
        '''
    },
    {
        'language': 'en',
        'title': 'Terms of Use',
        'slug': 'terms',
        'content': '''
<p>Welcome to law.co.il, the portal for information on law, computers and the Internet. Use of law.co.il or any part thereof (&quot;Site&quot; or &quot;law.co.il&quot;) is subject to these Terms of Use. Read the Terms carefully, as by using Site you agree to be bound by them.</p>
<p class="subtitle">About law.co.il</p>
<p>law.co.il&reg; is the first legal web site on Israeli Internet. It has been operating since March 1996, and is owned and managed by Adv. Haim Ravia (&quot;Site Manager&quot;). Questions related to Site may be addressed to Site Manager by means of <a href="office.php?d=e&amp;cat=2">this feedback form</a>.</p>
<p>Please note: use of Site is free of charge, but the liability of Site Manager is expressly limited as stated in these Terms of Use. Site Manager assume no liability whatsoever for any direct or indirect consequences of using information which is found through this site. The use of this site is subject to the Israeli law, and to the sole jurisdiction of the competent court in the district of Tel-Aviv-Jaffa (Israel). The use of this Site is subject to this disclaimer and attests to the user's agreement thereto.</p>
<p class="subtitle">Links on Site</p>
<p>On law.co.il&reg; you will find links and references to legal web sites and legal information on the Internet. Bear in mind that such sites and information are not made available by Site Manager, and Site Manager do not control or supervise them. Links to legal sites and information do not attest to their having been screened and found reliable, up-to-date, complete, or accurate. Furthermore, sites and information change and are updated frequently, whether due to legal innovations (especially in the dynamic areas covered by law.co.il) or to the ongoing changes typical of the Internet. Material that is up-to-date and complete today, may very well be inadequate or even false, tomorrow.</p>
<p>The online index featured under the tab &quot;Legal Links&quot; is edited at the subjective discretion of Site Manager. The order of appearance of sites listed in the index is not an indication of their quality or importance. Although Site Manager makes an effort to provide an adequate description of Sites listed in the index, they cannot ensure its being completely accurate or up-to-date.</p>
<p>Site Manager disclaims any warranty for the operability of the linked sites. Site Manager reserves the right to remove links previously displayed, or to refrain from adding new links, governed by his sole discretion. The fact that a link to a certain site is made available to you on law.co.il does not warrant that said link will not be removed or modified.</p>
<p>On law.co.il you will find news items and articles on legal aspects of IT and Internet. The articles, for the most part, were originally published in Globes, on the &quot;CyberLaw&quot; column, and in the Israel Bar Association magazine. They express solely the opinions of the writers, and do not claim to be complete, comprehensive, exhaustive or up-to-date. The content in said articles does not constitute legal advice.</p>
<p>The news items available on Site do not pertain to the Internet alone; they deal also with computers, electronic signature, free and open source software, telecommunications and other matters that are handled by Adv. Ravia. (obviously, from the legal perspective). Site Manager do not claim to display on Site &quot;all the news&quot; or the most important news, only what interests them and comes to their attention in the usual course of their work. Site Manager tries to keep the news feature updated on a regular basis, but this is not always possible. An attempt will be made to provide a reference for every item, and the accuracy of the item depends solely on the accuracy of the source. Should Site Manager happen to express an opinion, it is always to be taken as his own opinion only, not as a legal opinion or the opinion of his clients, law firm or firm's employees and partners.</p>
<p>It must be borne in mind that legal problems may have various solutions, depending on the nuances of each particular case. Moreover, some of the items and articles displayed on Site were originally published many years ago (from 1997). Every item and articles is clearly marked with the original date of publication. What was correct at the time is inadequate for present needs. Therefore, should a problem arise, similar to anything mentioned in the news items and articles on Site, a lawyer should be consulted; under no circumstances do the contents of law.co.il constitute a substitute for legal advice.</p>
<p class="subtitle">Legal forms</p>
<p>On law.co.il you will find a range of Hebrew legal forms. Choosing and completing legal forms requires professional expertise, and should be done by a lawyer; at the very least, the form should be reviewed by a lawyer before it is submitted to the authorities. Bear in mind that the particulars on the form may determine the applicant's rights!</p>
<p>Forms are occasionally updated, changed or replaced. Site Manager cannot guarantee that the forms appearing here will always be the most recent and correct versions. It is therefore necessary to verify the validity of a particular form, before deciding to use it. Should you find that a particular form is no longer up to date, please inform us by using the feedback form on this site.</p>
<p>The forms are designed for your personal use only or for use on a regular basis at a law firm. You may not use them for any commercial purpose or for profit, without obtaining in advance written permission from Site Manager.</p>
<p>By choosing one or more of the forms displayed on Site, storing them in your computer, or making use of them, you agree to be bound by the conditions stated in these Terms of Use. If you do not agree to these Terms, do not download, store or use the forms.</p>
<p class="subtitle">Mailing lists</p>
<p>Some of the information available at law.co.il is transmitted via email messages sent out from time to time, at intervals determined by Site Manager, to users who request to receive them. In order to receive this service you must submit an express request to subscribe. In the course of the subscription process you will be asked to provide Site Manager with your email address. You are requested to exercise caution in providing personal information, and to provide only accurate information. Site Manager will use the information you provide in accordance with the <a href="privacy.php?d=e">privacy policy</a> of law.co.il. You may stop receiving email messages at any time, of course.</p>
<p>Site Manager reserve the right to decide, at his sole discretion, not to provide this service to one or more its subscribers, or to terminate it altogether, for any reason whatsoever.</p>
<p class="subtitle">RSS Feeds</p>
<p>Some of the information on law.co.il is made avilable through RSS Feeds. When presented online, it is not permitted to include advertisements in the feeds or manipulate them otherwise. Site Manager reserves the right to require anyone who integrated such feed into a web site or any other online service to cease distributing the law.co.il content at any time for any reason.</p>
<p class="subtitle">Privacy</p>
<p>Site Manager respects the privacy of Site's users. The most recent Privacy Policy of law.co.il can always be found <a href="privacy.php?d=e">here</a>. It constitutes an integral part of these Terms of Use. Given that the Privacy Policy may occasionally change, it is recommended to re-read it from time to time.</p>
<p class="subtitle">Disclaimer of Liability</p>
<p>The information and services provided on Site are intended for use &quot;AS IS&quot;, and may not be adapted to the particular needs of this or that individual. Site Manager disclaims liability for any claim whatsoever, or any complaint or demand, arising from the use of the information or services provided on or via Site, or pertaining to their accuracy, reliability, completeness, timeliness or the frequency of their posting. The use of and reliance on the information available on Site is therefore entirely and solely your own responsibility.</p>
<p>Site mangers disclaim any liability, under any circumstances, arising on account of the legal information and sites linked from law.co.il, including the completeness, reliability, accuracy, and timeliness of such sites and information. Anyone relying on legal sites and legal information linked from law.co.il does so solely on his or her own responsibility.</p>
<p>The news items, articles, and columns on this site do not constitute legal advice and are not to be relied on as such. It is necessary to consult a lawyer for such reliance. Site Manager disclaim liability whatsoever for any outcome ensuing directly or indirectly from reliance on information made available on Site.</p>
<p>Site Manager disclaim any liability whatsoever for any outcome ensuing directly or indirectly arising from use of the Hebrew legal forms provided on Site. Use of the forms is done on the sole responsibility of the user.</p>
<p>Site Manager do not warrant uninterrupted operation of Site or its secure and smooth operation without glitches or failures of hardware, software, network cables and systems, experienced either by Site Manager or by any of their suppliers.</p>
<p>Site Manager disclaim any liability whatsoever arising from disclosure of particulars transmitted to Site in case of unlawful interception or intrusion into Site's computer systems.</p>
<p class="subtitle">Intellectual Property</p>
<p>All copyright and intellectual property rights on Site ? including news items, articles, format of the forms, and any other textual information of an kind whatsoever, the design of Site and all its contents, applications, computer code, graphic files and any other content included therein ? are owned solely by Site Manager . It is forbidden to copy, reproduce, distribute, display publicly, make available, translate or transmit to a third party, any part of the above without obtaining express written permission, in advance, from Site Manager .</p>
<p>law.co.il&reg; is a registered trademark of Haim Ravia, Adv. Site also operates under other domain names, such as cyberlaw.co.il, it-law.co.il and others. It is forbidden to use Site's domain names, the name &quot;Ravia&quot;, or the trademark law.co.il&reg;, without obtaining express written permission, in advance, from Site Manager.</p>
<p>Site may display content through agreement between Site Manager and third parties. The copyright to such content is owned by the third party that granted Site permission to use them. It is forbidden to copy, reproduce, distribute, display publicly, make available, translate or transmit these contents or any part thereof without express written permission, in advance, from the copyright owners.</p>
<p class="subtitle">Using Site</p>
<p>Site is designed for personal and private use only. It is forbidden to use the information and any other material on Site for commercial purposes. It is forbidden to display any data whatsoever displayed on Site on another Internet site or any other service, without obtaining written permission, in advance, from Site Manager, and subject to the conditions of such permission (should it be granted). It is likewise forbidden to store information and content displayed on Site through use of software such as Robots, Crawlers, etc., or to distribute such information and content commercially or via commercial means.</p>
<p>It is forbidden to display Site within a frame, whether visible or hidden.</p>
<p>It is forbidden to link Site's pages through &quot;deep links&quot;, unless the linking is to a full Web page, to be displayed to the user from Site's computers without any interference in its design, content or operation. &quot;Deep links&quot; are furthermore conditional upon the precise address of the page from Site appearing in the usual place appointed for it in the software used for viewing Site.</p>
<p>It is forbidden to link to isolate objects in Site, such as direct linking to images or documents displayed through Site.</p>
<p>It is forbidden to display Site with a different graphic design or interface than those defined for it by Site Manager, without obtaining written permission, in advance, from Site Manager.</p>
<p>It is forbidden to display Site through any technological systems whatsoever in such a way that modifies its content.</p>
<p class="subtitle">Termination of Use</p>
<p>Site Manager, at his sole discretion and without prior notice, may prevent you from using Site or any part thereof; prevent access to the entire site or parts thereof; cancel your subscription to services provided on Site; or remove or delete any information or content previously displayed on Site. In particular, Site Manager will do so in any case of violation of these Terms or in any case of omission or commission which causes or is likely to cause damage to Site, to its users, to Site Manager or anyone acting on their behalf. The provisions in this clause augment the rights of Site Manager by any law and by the other provisions of these Terms of Use.</p>
<p class="subtitle">Changes to Site</p>
<p>Site Manager may from time to time change Site's layout or display, as well as the scope and availability of the services provided therein and any aspect of them, without giving you prior notification. Such changes as may take place will take into account, inter alia, the dynamic nature of the Internet and the technological and other changes it is undergoing. Changes of this type by their very nature are likely to result in glitches or cause inconvenience of some kind. You shall have no claim of any kind whatsoever, or complain or demand, against Site Manager, ensuing from the introduction of aforesaid changes or from glitches or any kind of failure resulting from their introduction.</p>
<p class="subtitle">Termination of Site's operations</p>
<p>Site Manager may terminate Site's operations at any time, without prior notice, permanently or temporarily.</p>
<p class="subtitle">Indemnity</p>
<p>You agree to indemnify Site Manager, its managers, employees, operators, or anyone acting on their behalf, for any damages, loss of profit, loss of payable income, or expenses, including legal fees, they may incur due to the violation of these Terms of Use.</p>
<p class="subtitle">Changes to Terms of Use</p>
<p>Site Manager may from time to time change these Terms of Use without prior notice. You may at any time read the most recent version of the Terms of Use by clicking the appropriate link from Site pages.</p>
<p class="subtitle">Applicable Jurisdiction</p>
<p>These Terms of Use and the use of Site are subject to the laws of the State of Israel alone.</p>
<p>Any dispute between the parties, including disputes related to use of Site or to these Terms of Use, will fall under the sole jurisdiction of the competent court in the district of Tel Aviv, Israel.</p>
        '''
    },
    {
        'language': 'he',
        'title': 'מדיניות הפרטיות',
        'slug': 'privacy',
        'content': '''
        <p>law.co.il מופעל ומנוהל על-ידי עו&quot;ד חיים רביה. מדיניות הפרטיות של האתר פשוטה -</p>
<p>אנחנו לא אוספים מידע מזוהה אישית על משתמשי האתר, אלא אם כן הם פנו אלינו ביוזמתם ומסרו לנו את פרטיהם - לדוגמה, בעת הרשמה לרשימות הדיוור באתר או בעת משלוח הודעת דואר אלקטרוני אלינו, או בעקבות פניה באמצעות טופס המשוב המצוי באתר. במקרה כזה ישמרו פרטי הפונה במחשבי האתר או במחשבים שלנו עצמנו. אבל לא נעביר לשום צד שלישי את פרטיך או כל מידע אודותיך (ככל שפרטים ומידע זה מזהים אותך אישית), אלא במקרים אלה -</p>
<ul>
    <li>אם יתקבל בידינו צו שיפוטי שיורה לנו אחרת;</li>
    <li>בכל מחלוקת, טענה, תביעה, דרישה או הליכים משפטיים, אם יהיו, בינך לבינינו;</li>
    <li>אם נסבור שמסירת המידע נחוצה כדי למנוע נזק חמור לגופך או לרכושך או לגופו או לרכושו של צד שלישי;</li>
    <li>אם נעביר את ניהול האתר והפעלתו לגורם אחר, שאז נעביר אליו את פרטיך כדי שימשיך לספק לך את השירותים שביקשת.</li>
</ul>
<p class="subtitle">Cookies</p>
<p>האתר מיישם טכנולוגיה בשם PHP Session ID המיועדת לשמר מידע לצורך שימוש רצוף באתר. ה- Session ID יופיע כחלק מה-URL של האתר, בסרגל הכתובות (address bar) בדפדפן. ה- Session ID אינו מזהה אותך אישית. הוא גם פוקע ואינו נשמר לאחר שאתה סוגר את הדפדפן. במלים אחרות, כל עוד לא מסרת לנו מי אתה - אנחנו לא יודעים מי אתה. <br />
<br />
אבל יש שירותים שאנחנו משלבים באתר, והם משתמשים בעוגיות: שירותי הסטטיסטיקה של גוגל (ראו פרטים נוספים למטה), כפתורי ה- Like של פייסבוק ו- Google +1 של גוגל, וגם התוסף AddThis.</p>
<p class="subtitle">סטטיסטיקה</p>
<p>פעילות האתר מנוטרת באמצעות תוכנה המנתחת את יומני-המחשב שלו (ה'לוגים') ומפיקה מהם מידע סטטיסטי. מידע זה כולל נתונים כדוגמת מספר הביקורים באתר, המדורים שעניינו את המשתמשים, המדינות מהם הגיעו, מנועי החיפוש בהם השתמשו כדי לאתר את law.co.il, דפדפני האינטרנט שבעזרתם צפו באתר ועוד. המידע הנאסף הוא סטטיסטי בלבד. הוא איננו מזהה אותך אישית והוא נועד לצרכי ניתוח, מחקר ובקרה על פעילות האתר.</p>
<p>בנוסף, אנו משתמשים בשירותי הסטטיסטיקה של Google Analytics. לפי <a href="http://www.google.com/support/googleanalytics/bin/answer.py?answer=55539&amp;topic=10989">קובץ העזרה באתר גוגל</a>, שירותים אלה משתמשים בעוגיה ובקוד ג'אווה סקריפט כדי לאסוף מידע על הביקורים באתר. השירות מתחקה באופן אנונימי כיצד המבקרים באתר מתקשרים איתו, כולל מהיכן הגיעו ומה הם עשו באתר.</p>
<p class="subtitle">אבטחת מידע</p>
<p>במחשב המאחסן את האתר ובקוד-המחשב של האתר עצמו מיושמים עקרונות ומערכות לאבטחת מידע. בעוד שאלה מצמצמים את הסיכונים לחדירה בלתי-מורשית לאתר, אין בהם בטחון מוחלט. לכן, אנחנו לא מתחייבים שהאתר יהיה חסין באופן מוחלט מפני גישה בלתי-מורשית למידע שבו.</p>
<p class="subtitle">שינויים במדיניות הפרטיות</p>
<p>לבסוף, אנחנו רשאים לשנות מעת לעת את הוראות מדיניות הפרטיות בלא הודעה מוקדמת; אבל בכל עת, מדיניות הפרטיות העדכנית של האתר תתפרסם בו בגלוי.</p>
        '''
    },
    {
        'language': 'en',
        'title': 'Privacy Policy',
        'slug': 'privacy',
        'content': '''
 law.co.il&reg; (the &quot;Site&quot;) is operated and owned and managed by Adv. Haim Ravia. The privacy policy of Site is simple: <br />
<br />
We do not collect peronsally identifiable information on Site's users  <br />
<br />
There is a single exception to this rule, being that you yourself approach us of your own accord and provide us with personally identifying information, as, for example, through subscription to the mailing lists on Site, or as a result of contacting us via e-mail or using Site's feedback form. In this case, your personally identifying information will be stored, whether in Site's computers or with us. But we will not disclose your personally identifying information or personally identifying data regarding your activity on Site to a third party, except in the following cases:
<ul>
    <li>Should we are served with a court order to act otherwise;</li>
    <li>should any dispute arise, including any complaint, demand or legal processes, between yourself and us;</li>
    <li>should we believe that disclosing the information is necessary to protect your security or property, or those of a third party;</li>
    <li>should we transfer Site's management and operation to a third party, we may disclose to said third party your personally identifying information for the purpose of continuing to provide you with the services you requested.</li>
</ul>
Site implement the PHP Session ID technology designed to store information needed for continuous use of Site. Session ID appears as a part of Site URL, in your address bar. Session ID data does not identify you personally. It also expires and is not stored once you have exited Site. In other words, Site operators do not know who you are.  A cookie may be used by the Googl Anlytics service that monitors the site's usage and statistics. It may also be used by Facebook (we incorporate the &quot;Like&quot; button), Google, again, this time on account of the Google +1 button and AddThis which we incorporate on our news and articles' pages.<br />
<br />
Activity on Site is monitored through software that analyzes and processes its computer logs to derive statistics. It is also monitored by Google Anlytics statistics service. These statistics include, for example, the number of visitors to Site, the features that interested the users, the countries they are from, the search engine they used to find law.co.il&reg;, the Internet browsers they used to view Site and so on. The information collected is purely statistical. It does not identify you personally, and is meant for analysis, research and control of Site's activity. <br />
<br />
In the computer systems hosting Site, and in the source code of Site itself, measures has been taken to enhance data protection. While these reduce the risk of unlawful intrusion of Site, they do not provide total security. Therefore, we do not ensure absolute security against unlawful interception of information. <br />
<br />
We may from time to time change the provisions of this Privacy Policy without prior notice, but the most recent version of the Policy is always available for viewing on Site.
        '''
    },
    {
        'language': 'he',
        'title': 'אודות law.co.il',
        'slug': 'about',
        'content': '''
        <div style="float: right; text-align: center; margin-left: 20px;"><img src="/static/images/about_haim.jpg" alt="about haim" /><br />
<a href="office.php?d=h&amp;cat=21">עו&quot;ד חיים רביה</a></div>
<div style="line-height: 1.5em; margin-bottom: 60px;">law.co.il הוא האתר המשפטי הראשון בישראל. הוא כולל מידע על משפט באינטרנט, קניין רוחני, זכויות יוצרים, הגנת הפרטיות, דיני מחשבים, טכנולוגיה, קוד פתוח, חתימה אלקטרונית ודיני תקשורת. האתר הוקם בידי עו&quot;ד חיים רביה, במרץ 1996. הוא כולל אלפי ידיעות חדשותיות, מאמרים, פסקי-דין ותכנים ייחודיים אחרים בתחומים הללו - משפט באינטרנט, מחשבים, זכויות יוצרים, קוד פתוח, תקשורת, אבטחת מידע ופרטיות, חתימה אלקטרונית וקנין רוחני. חודשים אחדים לאחר שעלה לרשת החל האתר לפעול תחת שם המתחם הנוכחי, שהפך לשמו, ונרשם גם כסימן מסחרי. law.co.il הציע בתחילה קישורים משפטיים בשפה האנגלית בלבד ( באותן שנים עוד היה קשה להציג עברית באינטרנט...). מאז הפך למקור משפטי חשוב באינטרנט והוא מצוטט בפסקי-דין, מאמרים ועבודות אקדמאיות. באתר נרשמים עשרות אלפי ביקורים ייחודיים מדי חודש. רובם מישראל ואחרים מכל מדינות תבל (מארצות-הברית דרך ערב-הסעודית ועד לניו-זילנד).</div>
        ''',
    },
    {
        'language': 'en',
        'title': 'About law.co.il',
        'slug': 'about',
        'content': '''
   <div style="float: right; text-align: center; margin-left: 20px;"><img alt="about haim" src="/static/images/about_haim.jpg" /><br />
<a href="/en/office/lawyers/ravia/">Haim Ravia, Adv.</a></div>
<div>law.co.il&reg; is Israel's first legal web site. It is operated by Advocate Haim Ravia and contains thousands of Hebrew news items, articles, Israeli court decisions regarding computer law and the Internet, and other specialized content material related to his areas of expertise at <a href="http://www.pczlaw.com">Pearl Cohen Zedek Latzer Baratz </a>: Internet, IT, telecommunications, data protection and privacy, electronic signature and intellectual property. The Site is operated free of charge, as a public service, subject to its Terms of Use. Advocate Ravia launched the site on March 1996. Several months layer it began operating under its present domain and site names, law.co.il, a registered trademark. Initially offering legal links in English only (Hebrew web pages were practically nonexistent at the time), law.co.il has become a legal resource of prime importance on the Web, with 100,000 unique visits per month, mostly from Israel, others from all over the world - from the US to Saudi Arabia and New Zealand.</div>
        ''',
    },
    {
        'language': 'he',
        'title': 'אודות הקבוצה',
        'slug': 'about-group',
        'content': '''
   <div style="line-height: 1.5em;"><img src="/static/images/lobby.jpg" alt="Pearl Cohen Zedek Herzelia Office" style="float: left; margin-right: 20px;" /> 				קבוצת האינטרנט, הסייבר וזכויות היוצרים ב<a href="http://www.pczlaw.com">פרל כהן צדק לצר ברץ</a>&nbsp;(בעבר היתה הקבוצה משרד עו&quot;ד עצמאי, רביה ושות', עורכי דין) עוסקת  בסוגיות, המתעוררות בעת שימוש במערכות מחשב ואינטרנט, ונמצאות בחזית הידע המשפטי: <a href="office.php?d=h&amp;cat=11">משפט באינטרנט</a>,&nbsp;<a href="office.php?d=h&amp;cat=15">סייבר, אבטחת מידע ופרטיות</a>,&nbsp;<a style="line-height: 1.5em;" href="office.php?d=h&amp;cat=12">דיני וחוזי מחשבים</a><span style="line-height: 1.5em;">, </span><a style="line-height: 1.5em;" href="office.php?d=h&amp;cat=13">חתימה אלקטרונית</a><span style="line-height: 1.5em;">, </span><a style="line-height: 1.5em;" href="office.php?d=h&amp;cat=14">תקשורת</a><span style="line-height: 1.5em;">, </span><span style="line-height: 1.5em;">זכויות יוצרים ו</span><a style="line-height: 1.5em;" href="office.php?d=h&amp;cat=16">קניין רוחני</a><span style="line-height: 1.5em;"> - כל זאת לצד עיסוק בתחומים משלימים כדוגמת </span><a style="line-height: 1.5em;" href="office.php?d=h&amp;cat=17">משפט אזרחי ומסחרי</a><span style="line-height: 1.5em;"> וייצוג והופעות בבתי משפט. שורשיה במשרד עורכי הדין רביה ושות', שהיה הראשון בארץ להתמקד בנושאים אלה. גם אתר האינטרנט של עו&quot;ד חיים רביה העומד בראש הקבוצה, שבו הנך מצוי כעת, היה האתר המשפטי הראשון בארץ. הוא פועל מאז חודש מרץ 1996.&nbsp;</span></div>
<div style="line-height: 1.5em;"><br />
במרוצת השנים טיפלו עורכי הדין בקבוצה הן ב<strong>עסקאות גדולות</strong> בתחומי ההתמחות של הקבוצה (כדוגמת הקמת וניהול אתרי סחר אלקטרוני ותוכן מהגדולים בישראל, פיתוח מערכות מחשב ועוד), הן ב<strong>חוות-דעת מורכבות</strong> בנושאים חדשניים והן ב<strong>הליכים משפטיים</strong> (כדוגמת התביעות התקדימיות בנושאי האזנת סתר לדואר אלקטרוני ודואר זבל באינטרנט) - כל זאת לצד <strong>שירותים משפטיים שוטפים</strong> ללקוחות המשרד.  				<br />
<br />
<img src="/static/images/conference_room.jpg" alt="Pearl Cohen Zedek Herzelia Office" style="float: left; margin-right: 20px; margin-bottom: 30px;" class="bottom" /> 				הקבוצה מספקת את שירותיה ל<strong>מגוון רחב של לקוחות</strong>: החל מ<strong>חברות ענק בינלאומיות </strong>ו<strong>החברות הגדולות במשק</strong> הישראלי ועד ל<strong>חברות-הזנק ('סטארט אפים') </strong>ו<strong>יזמים פרטיים</strong> - חברות תוכנה וסייבר, בנקים וגורמים פיננסיים, חברות ביטוח, רשתות קמעונאיות, בעלי וארגוני זכויות יוצרים, רשתות חינוך, אתרי-סף ('פורטלים') ואתרי תוכן באינטרנט, מיזמי סחר אלקטרוני, חברות שירותים הפועלות בתחומי המחשב והאינטרנט, הוצאות לאור, ארגון ענפי, חברות טכנולוגיה ולמידה מרחוק ועוד. 				<br />
        ''',
    },
    {
        'language': 'en',
        'title': 'About the Group',
        'slug': 'about-group',
        'content': '''
 <div style="line-height: 1.5em"><img src="/static/images/lobby.jpg" alt="Pearl Cohen Zedek Herzelia Office" style="float: left; margin-right: 20px" /> The Internet, Cyber &amp; Copyright Group at <a href="http://www.pczlaw.com">Pearl Cohen Zedek Latzer Baratz</a> is a leading legal group in Israel, specializing in the law relating to computers, the Internet and information technology. Its roots lies in Ravia &amp; Co., Law Offices, one of the first in this field in Israel.The Internet site, which you are now visiting, was the first legal site in Israel, launched in March 1996. <br />
<br />
Over the years, the attorneys at the Internet, Cyber &amp; Copyright group have handled large-scale transactions in the group's areas of expertise. Such transactions include legal aspects of construction and management of some of the biggest e-commerce and content sites in Israel and development of IT systems. The group also represents its clients in legal procedures, such as the precedent-setting lawsuits about e-mail eavesdropping and electronic junk mail. Complex legal opinions regarding innovative issues of Cyberlaw, Privacy &amp; Data Protection, Computer Law, Electronic Signature, Intellectual Property &amp; Telecommunication Law complement the groups's services together with legal services needed for the everyday operation of business in Israel. <br />
<br />
<img src="/static/images/conference_room.jpg" alt="Pearl Cohen Zedek Herzelia Office" class="bottom" style="margin-bottom: 30px; float: left; margin-right: 20px" /> The group serves a wide range of clients: multinational companies,&nbsp;some of the biggest corporations in Israel, start-ups and private entrepreneurs: these include Cyber and Software companies, Internet Service Providers, banks and financial institutions, insurance companies, retail chains engaging in online sales, copyright owners (both individuals and organizations), portals and content sites, e-commerce ventures, companies offering computer and Internet services, publishers, employees organization, technology and distance-learning companies, etc. <br />
        ''',
    },
]


def load_pages(apps, schema_editor):
    Page = apps.get_model('pages', 'Page')
    pages = [Page(**page) for page in PAGES]
    Page.objects.bulk_create(pages)


def unload_pages(apps, schema_editor):
    Page = apps.get_model('pages', 'Page')
    slugs = set([x['slug'] for x in PAGES])
    Page.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160705_1144'),
    ]

    operations = [
        migrations.RunPython(load_pages, reverse_code=unload_pages)
    ]
