import requests
data = '''" <https://partners.kidpass.com/>        YOU HAVE A BOOKING

  
  Attendee: Xander

  Child's Age: 9 years 
 Parent/Guardian: Susan Millius   
 Email: susanmillius@yahoo.com 
 Phone: +15188284958 
 Confirmation Number: 169516787 
 
  Guitar Explorers - Free Guitar Class
<https://kidpass.com/activities/11412/41807/169516787> 
 Pixical <https://kidpass.com/providers/11412> 
 Fri 1/28, 4:00 PM - 4:30 PM PST 
      MANAGE BOOKINGS <https://partners.kidpass.com/>
<http://www.instagram.com/kidpass> <http://www.facebook.com/kidpass>
<http://www.twitter.com/kidpass> <https://blog.kidpass.com/>
<https://itunes.apple.com/us/app/kidpass/id1090085940>
<https://play.google.com/store/apps/details?id=com.kidpass.kidpass> 
© 2022 KIDPASS, INC. 
335 Madison Ave, 7th Floor, New York, NY 10017 
 
You are receiving this email because you partner with KidPass. To view your
schedules, log in <https://partners.kidpass.com/> to your account where you
can manage your bookings.
 
Privacy Policy <https://kidpass.com/privacy> | Terms Of Service
<https://kidpass.com/terms>
"'''
# headers = {
#   "X-CleverTap-Account-Id": "8WR-899-KR6Z",
#   "X-CleverTap-Passcode": "SCY-KUV-GWUL",
#   "Content-Type": "application/json; charset=utf-8",
# }
# data = '''{
#    "d":[{
#       "identity":"pixtest@gmail.com",
#       "ts":1636701907,
#       "evtName":"pixemy mini slot booked",
#       "type":"event",
#       "evtData":{
#          "category":"art",
#          "courseTitle":"Learn To Draw A Cartoon Animal Character",
#          "courseUrl":"https://pixemy.com/minis-detail/learn-to-draw-a-cartoon-animal-character-by-danielle-hruska",
#          "feedbackForm":"insert feedback form link",
#          "learningMaterial":"insert learning material link",
#          "lessonNumber":"1",
#          "page":"minis course details page",
#          "slotDate":"November 5rd, 5 PM PDT",
#          "teacherName":"Danielle Hruska"
#       }
#    }]
# }'''
data = data.encode(encoding='utf-8')

requests.post('http://127.0.0.1:5000/uploaded', data)
# print(requests.post("https://api.clevertap.com/1/upload", data, headers=headers).json())