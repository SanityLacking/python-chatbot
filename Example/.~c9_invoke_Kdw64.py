# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from translate import Translator
from korean import Noun

responsek=' '
# Create a new instance of a ChatBot
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'Can you please make your question more specific?'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

def train():
      # Train the chat bot with a few responses
      bot.train([
        'how can I go to iae eduhouse',#get to iae eduhouse, address iae eduhouse, where iae eduhouse
        '서울특별시 강남구 테헤란로 120(역삼동 824-20) 상경빌딩 5층',
        #2
        'information about study abroad',# application information, yuhak information, prepare yuhak
        '유학 신청과정은 아래의 웹에 자세히 나와 있습니다.: http://www.eduhouse.net/talk/talk_guide_univ.asp',
        #3
        'when is the application deadline',# application deadline, application due
        '유학 신청마감,유학 신청과정은 아래의 웹에 자세히 나와 있습니다.: http://www.eduhouse.net/talk/talk_guide_univ.asp',
        #4
        'How much english score do I need', #ielts score, toefl score, english score
        '호주의 대학에 가려면, IELTS 평균 6.5 이상이 되어야 합니다. 그리고 모든 과목이 6.0이상이 되어야 합니다.',
        #5
        'toefl for admission',
        '호주에서는 TOEFL 시험보다는 IELTS 시험이 더 많이 사용되고 일반적입니다. TOEFL 시험과는 다르게 IELTS 시험은 IELTS Academic과 IELTS General 두 가지가 있으며 대학에 지원할 때는 IELTS Academic 시험을 봐야 합니다. 그러나 모든 대학에서는 IELTS 시험과 함께 TOEFL 시험, Cambridge 시험, PTE 시험 등 다양한 공식 영어시험들도 인정하고 있습니다.',
        #6
        'english university without IELTS',#without ielts, low score, not enough score
        '만약 현재 본인이 충분한 영어실력이 있다면 가장 좋은 방법은 IELTS나 TOEFL과 같은 공식 영어시험에 응시하여 점수를 취득하는 것이 가장 좋습니다. 그러나 현재 영어실력이 부족하다면 진학하고자 하는 대학 내 대학부설 영어과정이나 해당 대학과 연계되어 있는 사설 영어교육기관에서 영어연수과정을 수강한 후 대학으로 진학할 수 있습니다. 이 경우 대학입학을 위해 정해진 레벨을 마치면 IELTS나 TOEF과 같은 공식 영어시험 제출 없이 진학할 수 있습니다.',
        #7
        'recommend prestigious australian universities', #recommend universities, high level universities, good universities, recommend pretigious universities
        '호주에는 호주의 아이비리그라고 알려진 그룹 오브 에이트(Group of Eight, Go8) 대학들이 있습니다. 호주 대학 랭킹에서 늘 1윌부터 8위까지를 차지하는 8개 대학으로 호주 국립대학교(Australian National University, ANU), 뉴 사우스 웨일즈 대학교(University of New South Wales, UNSW), 퀸즐랜드 대학교(University of Queensland, UQ), 모나쉬 대학교(Monash University), 서호주 대학교(University of Western Australia, UWA), 아들레이드 대학교(University of Adelaide), 시드니 대학교(University of Sydney), 멜번 대학교(University of Melbourne)입니다. 이 8개 대학은 모든 교육과정이 전반적으로 수준이 높고 우수하며, 분야별 대학 랭킹에서도 각 분야에서 상위권에 올라있습니다. 그러나 일부 특정한 학과나 분야에서는 이 대학보다 상위에 랭크 되어 있는 다른 유명한 대학들도 있습니다. 예를 들어 호텔관광(Hospitality) 분야에서는 그리피스 대학교(Griffith University), 스포츠 과학(Sport Science) 분야에서는 디킨 대학교(Deakin University)가 호주 내 1위로 가장 유명합니다.',
        #8
        'bachelor degree', #undergraduate 
        '호주에는 호주의 아이비리그라고 알려진 그룹 오브 에이트(Group of Eight, Go8) 대학들이 있습니다. 호주 대학 랭킹에서 늘 1윌부터 8위까지를 차지하는 8개 대학으로 호주 국립대학교(Australian National University, ANU), 뉴 사우스 웨일즈 대학교(University of New South Wales, UNSW), 퀸즐랜드 대학교(University of Queensland, UQ), 모나쉬 대학교(Monash University), 서호주 대학교(University of Western Australia, UWA), 아들레이드 대학교(University of Adelaide), 시드니 대학교(University of Sydney), 멜번 대학교(University of Melbourne)입니다. 이 8개 대학은 모든 교육과정이 전반적으로 수준이 높고 우수하며, 분야별 대학 랭킹에서도 각 분야에서 상위권에 올라있습니다. 그러나 일부 특정한 학과나 분야에서는 이 대학보다 상위에 랭크 되어 있는 다른 유명한 대학들도 있습니다. 예를 들어 호텔관광(Hospitality) 분야에서는 그리피스 대학교(Griffith University), 스포츠 과학(Sport Science) 분야에서는 디킨 대학교(Deakin University)가 호주 내 1위로 가장 유명합니다.',
        #9
        'finish high school in korea and enter australia university',
        '한국에서 고등학교만 마친 학생들은 한국 대학교 1학년에 해당하는 학부예비과정(Foundation)을 수강한 후 호주 대학교 1학년으로 진학하거나, 디플로마(Diploma) 과정을 수강한 후 호주 대학교 2학년으로 편입하는 방법 중 한가지를 선택할 수 있습니다. 호주의 교육시스템은 한국과 다릅니다. 한국 대학교에서의 1학년 과정을 호주에서는 11학년과 12학년때 배우며, 호주 대학교 1학년과정은 한국 대학교 2학년 과정과 동일하다고 할 수 있습니다. 호주 대학교의 학사과정들이 대부분 3년 과정인 것은 이러한 이유 때문입니다. 따라서 호주 대학교 1학년에 바로 입학하는 기본 학력 조건은 한국 대학교에서 1학년을 마친 학생입니다. 그러나 한국에서 고등학교만 졸업한 학생이어도 고등학교 성적이 우수한 경우라면 예외적으로 호주 대학으로 바로 입학할 수도 있습니다.',
        #10
        'international student to enter Australian school', #enter, entrance
        '호주 교육부를 통해서 공립학교에 입학할 수 있습니다. 단, 공립학교는 지역별로 학업수준이 크게 다를 수 있습니다. 따라서 생활비가 좀 더 들더라도 좋은 지역으로 가서 학업수준이 높은 학교에 다닐 수 있도록 할 것을 권장합니다.',
        #11
        'after australia high school university other country', #after australian high school to enter, USA, Canada, america
        '가능합니다. 그러나 각 국가에서 요구하는 특정한 입학조건이 있을 경우 미리 준비해야 합니다. 예를 들어 미국과 같은 경우 우수한 대학들은 대부분 SAT 점수를 요구하기 때문에 SAT 시험을 미리 준비해야 하며, 이는 한국에서 해외대학으로 진학할 때도 마찬가지 입니다.',
        #12
        'universit cost', # cost, tuition fee
        '대학교 학비는 대학별 또는 학업 분야별로 큰 차이가 있습니다. 호주 8대 명문이라는 Go8 대학들은 연간 AUD 30,000-40,000 수준이며, 대도시를 벗어난 중소도시에 위치한 대학들은 연간 AUD 20,000-AUD 35,000 수준이라고 볼 수 있습니다. 그러나 같은 대학이라도 학업 분야별로 차이가 있으며, 예를 들어 의과대학은 대부분이 연간 AUD 60,000 정도 입니다.',
        #13
        'living cost', #living cost, living expense
        '일반적으로는 매월 약 AUD 1,200-1,500 정도가 든다고 할 수 있지만, 살고 있는 도시와 생활습관에 따라 천차만별입니다. 특히 호주 내 생활비에서 가장 큰 비중을 차지하는 렌트비는 시드니, 멜번, 브리즈번과 같은 대도시와 소도시의 차이가 매우 큽니다. 예를 들어 원룸을 렌트하는 경우 시드니에서 적어도 주당 AUD 450의 비용이 들지만, 뉴카슬에서는 주당 AUD 270 정도입니다.',
        #14
        'study without student visa',
        '관광비자인 경우 최대 12주까지 공부할 수 있으며, 12주보다 더 길게 공부하고 싶으면 학생비자가 필요합니다.',
        #15
        'age limit working holiday',
        '호주 정부에서 워킹 홀리데이 비자의 나이제한을 만 30세에서 만 35세로 확대할 계획이라고 발표했습니다. 그러나 현재 나이조건은 변경되지 않았으며, 여전히 만 30세까지 입니다. 협력국들과의 협의를 통해 점진적으로 이루어질 예정이라고 합니다.',
        #16
        'how long stay with working holiday visa',
        '호주 워킹홀리데이 비자 기간은 1년입니다. 단 정해진 조건을 충족하는 경우 1회 연장 하여 1년의 기간을 더 받을 수 있습니다.',
        #17
        'period working holiday visa',
        '워킹 홀리데이 비자 기간 워홀 ,호주 워킹홀리데이 비자 기간은 1년입니다. 단 정해진 조건을 충족하는 경우 1회 연장 하여 1년의 기간을 더 받을 수 있습니다.',
        #18
        'study with working holiday visa',
        '최대 17주까지 호주에서 합법적으로 공부할 수 있습니다.',
        #19
        'how much payment work part time',
        '현재 호주의 최저 임금은 시간당 AUD 18.29 입니다. 만약 주당 20시간의 파트타임으로 일하면 주당 AUD 365.8을 벌 수 있으며, 한화로는 약 33만원 정도입니다. 이는 최저임금으로 계산했을 경우이며, 업무에 따라 혹은 일하는 시간대에 따라 이보다 더 높을 수도 있습니다.',
        #20
        'part time work in australia',
        '현재 호주의 최저 임금은 시간당 AUD 18.29 입니다. 만약 주당 20시간의 파트타임으로 일하면 주당 AUD 365.8을 벌 수 있으며, 한화로는 약 33만원 정도입니다. 이는 최저임금으로 계산했을 경우이며, 업무에 따라 혹은 일하는 시간대에 따라 이보다 더 높을 수도 있습니다.',
        #21
        'receive student visa',
        '일반적으로 신청 후 2주에서 4주 정도 걸립니다. 단, 상황에 따라 약간 더 길어질 수도 있습니다.',
        #22
        'student visa application',
        '일반적으로 신청 후 2주에서 4주 정도 걸립니다. 단, 상황에 따라 약간 더 길어질 수도 있습니다.',
        #23
        'change tourist visa',
        '바꿀 수 있습니다. 만약 처음에는 단기간 공부할 생각으로 혹은 여행만 할 생각으로 관광비자로 입국했지만, 마음이 변해 12주 이상의 학업을 진행하게 된 경우 호주 내에서 관광비자를 학생비자로 바꿀 수 있습니다.',
        #24
        'change working holiday visa',
        '바꿀 수 있습니다. 만약 학생비자 신청 후 수령하기 전에 보유하고 있던 워킹 홀리데이 비자가 끝나는 경우에는 학생비자 수령을 기다리는 기간 동안 호주에 합법적으로 머무를 수 있도록 하는 브릿징 비자(Bridging Visa)를 받을 수 있습니다. 그러나 가능하면 충분한 기간을 두고 학생비자를 신청하여 받을 수 있도록 할 것을 권장합니다.',
        #25
        'job after finish study',
        '기본적으로 호주에서 2년 이상의 학업을 마치면 일정 기간의 취업비자를 받아서 합법적으로 일을 할 수 있습니다. 학사과정이나 수업위주의 석사과정(Coursework)을 마치면 2년, 연구석사과정(Research)이나 박사과정을 마치면 4년의 취업비자를 받을 수 있습니다. TAFE에서 2년 이상의 과정을 마친 경우에는 본인이 공부한 분야의 기술 평가(skills assessment)를 통과한 경우 1년 6개월의 취업비자를 받을 수 있습니다.',
        #26
        'can work after finish study',
        '기본적으로 호주에서 2년 이상의 학업을 마치면 일정 기간의 취업비자를 받아서 합법적으로 일을 할 수 있습니다. 학사과정이나 수업위주의 석사과정(Coursework)을 마치면 2년, 연구석사과정(Research)이나 박사과정을 마치면 4년의 취업비자를 받을 수 있습니다. TAFE에서 2년 이상의 과정을 마친 경우에는 본인이 공부한 분야의 기술 평가(skills assessment)를 통과한 경우 1년 6개월의 취업비자를 받을 수 있습니다.',
        #27
        'time difference australia korea',# time difference
        '호주는 한국과 달리 땅이 넓어서 호주 내에서도 시차가 있습니다. 대도시를 기준으로 시드니와 멜번, 브리즈번은 한국보다 1시간이 빠르고, 아들레이드는 한국보다 30분이 빠르며, 퍼스는 한국보다 1시간이 느립니다. 즉 대부분이 30분에서 1시간 정도의 차이로 한국과 큰 차이는 없습니다.',
        #28
        'helloo',
        '안녕하세요?',
        #29
        'how are you',
        '안녕하세요?',
        #30
        'thanks',
        '천만에요'
      ])

#while True:
# Get a response for some unexpected input
#response = bot.get_response('How do I make an omelette?')
 #     entered_input = input("Please enter your text: ")
def search(entered_input):
      #haystack = entered_input
      translator= Translator(to_lang="en")
      entered_input = translator.translate(entered_input)
      entered_input = entered_input.lower()
      print(entered_input)
      haystack = entered_input

      if (haystack.find('toefl')>=0 and haystack.find('admission')>=0) or (haystack.find('ielts')>=0 and haystack.find('admission')>=0) or (haystack.find('english')>=0 and haystack.find('admission')>=0):
            haystack='toefl for admission'
      elif (haystack.find('university')>=0 or haystack.find('college')>=0) and haystack.find('without')>=0 and (haystack.find('ielts')>=0 or haystack.find('toefl')>=0 or haystack.find('english')>=0):
            haystack='english university without IELTS'
      elif (haystack.find('english')>=0 and haystack.find('require')>=0) or (haystack.find('english')>=0 and haystack.find('prerequisit')>=0):
            haystack='english university without IELTS'
      elif haystack.find('enough score')>=0 or haystack.find('low score')>=0:
            haystack='how much english score do I need'
      elif haystack.find('english')>=0 or haystack.find('toefl')>=0 or haystack.find('ielts')>=0:
            haystack='how much english score do I need'
#
      elif haystack.find('student visa')>=0 and haystack.find('appl')>=0:
            haystack='student visa application'
      elif haystack.find('student visa')>=0 and haystack.find('receiv')>=0:
            haystack='receive student visa'
      elif haystack.find('study')>=0 and haystack.find('student visa')>=0 and haystack.find('without')>=0:
            haystack='study without student visa'
      elif haystack.find('change')>=0 and haystack.find('working holiday')>=0 or haystack.find('byeongyeong')>=0:
            haystack='change working holiday visa'
      elif haystack.find('change')>=0 and (haystack.find('tourist')>=0 or haystack.find('byeongyeong')>=0):
            haystack='change tourist visa'
      elif haystack.find('change')>=0 and haystack.find('visa')>=0:
            haystack='change working holiday visa'
      elif haystack.find('working holiday')>=0 and haystack.find('visa')>=0 and haystack.find('stay')>=0:
            haystack='how long stay with working holiday visa'
      elif haystack.find('working holiday')>=0 and haystack.find('visa')>=0 and (haystack.find('long')>=0 or haystack.find('duration')>=0 or haystack.find('period')>=0):
            haystack='period working holiday visa'
      elif haystack.find('study')>=0 and haystack.find('working holiday')>=0 and haystack.find('visa')>=0:
            haystack='study with working holiday visa'
      elif haystack.find('age')>=0 and haystack.find('working holiday')>=0 and haystack.find('visa')>=0:
            haystack=' age limit working holiday'
      elif (haystack.find('work')>=0 or haystack.find('much')>=0 or haystack.find('pay')>=0 or haystack.find('paid')>=0) and haystack.find('part')>=0 and haystack.find('time')>=0:
            haystack='part time work in australia'
      elif haystack.find('job')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0:
            haystack='part time work in australia'
      elif haystack.find('work')>=0 and haystack.find('study')>=0 and (haystack.find('during')>=0 or haystack.find('while')>=0):
            haystack='work while study'
      elif (haystack.find('work')>=0 or haystack.find('job')>=0) and haystack.find('after')>=0 and (haystack.find('graduate')>=0 or :
            haystack='work after finish study'
      elif haystack.find('international')>=0 and haystack.find('school')>=0 and haystack.find('australia')>=0:
            haystack='international student to enter australian school'
      elif haystack.find('international')>=0 and haystack.find('middle')>=0:
            haystack='international student middle school'
      elif (haystack.find('best')>=0 or haystack.find('rank')>=0 or haystack.find('prestigious')>=0  or haystack.find('level')>=0  or haystack.find('good')>=0  or haystack.find('recommend')>=0) and haystack.find('universit')>=0:
            haystack='recommend prestigious australian university'
      elif haystack.find('high')>=0 and haystack.find('school')>=0 and haystack.find('australia')>=0 and haystack.find('universit')>=0 and (haystack.find('countr')>=0 or haystack.find('usa')>=0 or haystack.find('canada')>=0 or haystack.find('america')>=0):
            haystack='after australia high school university other country'
      elif haystack.find('school')>=0 and haystack.find('entrance')>=0:
            haystack='international student to enter australian school'
      elif haystack.find('high')>=0 and haystack.find('school')>=0 and haystack.find('korea')>=0 and haystack.find('universit')>=0 and haystack.find('australia')>=0:
            haystack='finish high school in korea and enter australia university'
      elif haystack.find('high')>=0 and haystack.find('school')>=0 and haystack.find('korea')>=0:
            haystack='high school korea'
      elif haystack.find('living')>=0 and (haystack.find('year')>=0 or haystack.find('cost')>=0 or haystack.find('annual')>=0):
            haystack='living cost'
      elif haystack.find('living')>=0 and haystack.find('expen')>=0:
            haystack='living expense'
      elif haystack.find('university')>=0 and (haystack.find('fee')>=0 or  haystack.find('cost')>=0):
            haystack='universit cost'
      elif haystack.find('fee')>=0:
            haystack='tuition fee'
      elif haystack.find('study abroad')>=0 or (haystack.find('study')>=0 and haystack.find('foreign')>=0) or (haystack.find('study')>=0 and haystack.find('overseas')>=0):
            haystack='information about study abroad'
      elif haystack.find('abroad')>=0 or haystack.find('foreign')>=0 or haystack.find('overseas')>=0 or haystack.find('yuhak')>=0:
            haystack='information about study abroad'
      elif haystack.find('study')>=0 and haystack.find('australia')>=0:
            haystack='study in australia'
      elif haystack.find('application')>=0 and (haystack.find('application')>=0 or haystack.find('due')>=0):
            haystack='when is the application deadline'
      elif haystack.find('iae eduhouse')>=0 and (haystack.find('address')>=0 or haystack.find('where')>=0 or haystack.find('location')>=0):
            haystack='how can I go to iae eduhouse'
      elif haystack.find('iae eduhouse')>=0:
            haystack='how can I go to iae eduhouse'
      elif haystack.find('time')>=0 and haystack.find('australia')>=0 and haystack.find('korea')>=0:
            haystack='time difference australia korea'
      elif haystack.find('time')>=0 and haystack.find('difference')>=0:
            haystack='time difference'
      elif haystack.find('bachelor')>=0 or haystack.find('undergrad')>=0:
            haystack='bachelor degree'
      elif haystack.find('hi ')>=0 or haystack.find('hello')>=0 or haystack.find('molayo')>=0:
            haystack='helloo'
      elif haystack.find('how are you')>=0 or haystack.find('understand/ok')>=0 or haystack.find('well')>=0:
            haystack='how are you'
      elif haystack.find('thank')>=0:
            haystack='thanks'
#      else:
#            haystack='Can you please make your question more specific?'
  
      response = bot.get_response(haystack)
      #response=str(responsek)+'\n\n'+str(response2)
      print(haystack)
      print(response)
      return(response)

#response = bot.get_response(entered_input)
#print(response)
