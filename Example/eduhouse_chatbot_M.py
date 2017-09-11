# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from translate import Translator
from korean import Noun
from Example.data_formatter import Data_Formatter

formatter = Data_Formatter('Example/Eduhouse.csv')

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
      bot.train(formatter.get_training_array()[1])

#while True:
# Get a response for some unexpected input
#response = bot.get_response('How do I make an omelette?')
 #     entered_input = input("Please enter your text: ")
def search(entered_input):
      #haystack = entered_input
      translator= Translator(to_lang="en")
      entered_input = translator.translate(entered_input)
      print(entered_input)
      entered_input = entered_input.lower()
      haystack = entered_input

      if haystack.find('toefl')>=0:
            haystack='toefl exam'
            responsek='호주의 IELTS는 TOEFL보다 일반적인 영어 시험입니다. TOEFL과 달리 IELTS에는 IELTS Academic과 IELTS General의 두 가지 유형이 있지만 대학에 가면 IELTS Academic을 선택해야합니다. 대부분의 대학은 TOEFL, Cambridge, PTE 등도 수락합니다.'
      elif haystack.find('ielts')>=0:
            haystack='ielts'
            responsek='하위 점수가 6.0 미만인 IELTS (아카데믹)의 최소 종합 점수 6.5'
      elif haystack.find('pte')>=0:
            haystack='pte'
            responsek='호주의 IELTS는 TOEFL보다 일반적인 영어 시험입니다. TOEFL과 달리 IELTS에는 IELTS Academic과 IELTS General의 두 가지 유형이 있지만 대학에 가면 IELTS Academic을 선택해야합니다. 대부분의 대학은 TOEFL, Cambridge, PTE 등도 수락합니다.'
      elif haystack.find('university')>=0 and haystack.find('without')>=0 and haystack.find('english')>=0:
            haystack='english university without'
            responsek='영어가 충분하다면 공식 영어 시험을 볼 수 있습니다. 그러나 그렇지 않은 경우 대학에 소속 된 영어 연수 기관이나 귀하가 들어가고 자하는 대학교와 파트너 관계를 유지하고있는 사립 영어 연수 기관에서 영어 수업을 받아야합니다. 그리고 특정 레벨의 영어를 마치면 IELTS 나 TOEFL과 같은 공식 영어 시험없이 대학에 입학 할 수 있습니다'
      elif haystack.find('college')>=0 and haystack.find('without')>=0 and haystack.find('english')>=0:
            haystack='english university without'
            responsek='영어가 충분하다면 공식 영어 시험을 볼 수 있습니다. 그러나 그렇지 않은 경우 대학에 소속 된 영어 연수 기관이나 귀하가 들어가고 자하는 대학교와 파트너 관계를 유지하고있는 사립 영어 연수 기관에서 영어 수업을 받아야합니다. 그리고 특정 레벨의 영어를 마치면 IELTS 나 TOEFL과 같은 공식 영어 시험없이 대학에 입학 할 수 있습니다'
      elif haystack.find('english')>=0 and haystack.find('require')>=0:
            haystack='english require'
            responsek='하위 점수가 6.0 미만인 IELTS (아카데믹)의 최소 종합 점수 6.5'
      elif haystack.find('english')>=0 and haystack.find('prerequisit')>=0:
            haystack='english prerequisit'
            responsek='하위 점수가 6.0 미만인 IELTS (아카데믹)의 최소 종합 점수 6.5'
      elif haystack.find('language')>=0 and haystack.find('university')>=0 and haystack.find('without')>=0:
            haystack='language university without'
            responsek='영어가 충분하다면 공식 영어 시험을 볼 수 있습니다. 그러나 그렇지 않은 경우 대학에 소속 된 영어 연수 기관이나 귀하가 들어가고 자하는 대학교와 파트너 관계를 유지하고있는 사립 영어 연수 기관에서 영어 수업을 받아야합니다. 그리고 특정 레벨의 영어를 마치면 IELTS 나 TOEFL과 같은 공식 영어 시험없이 대학에 입학 할 수 있습니다.'
      elif haystack.find('language')>=0 and haystack.find('require')>=0:
            haystack='language require'
            responsek='하위 점수가 6.0 미만인 IELTS (아카데믹)의 최소 종합 점수 6.5'
      elif haystack.find('language')>=0 and haystack.find('prerequisit')>=0:
            haystack='language prerequisit'
            responsek='하위 점수가 6.0 미만인 IELTS (아카데믹)의 최소 종합 점수 6.5'
      elif haystack.find('student visa')>=0 and haystack.find('long')>=0 and haystack.find('after')>=0 and haystack.find('appl')>=0:
            haystack='Student visa long after appl'
            responsek='일반적으로 신청 후 약 2 ~ 4 주가 소요되며 때로는 약간 더 오래 걸릴 수도 있습니다'
      elif haystack.find('student visa')>=0 and haystack.find('time')>=0 and haystack.find('after')>=0 and haystack.find('appl')>=0:
            haystack='Student visa time after appl'
            responsek='일반적으로 신청 후 약 2 ~ 4 주가 소요되며 때로는 약간 더 오래 걸릴 수도 있습니다'
      elif haystack.find('student visa')>=0 and haystack.find('visitor')>=0:
            haystack='Student visa visitor'
            responsek='단기간에 공부할 계획이라면 공부를 연장하기 위해 호주에서 학생 비자로 변경할 수 있습니다.'
      elif haystack.find('student visa')>=0 and haystack.find('change')>=0 and haystack.find('working holiday')>=0 and haystack.find('visa')>=0:
            haystack='Student visa working holiday visa'
            responsek='귀하는 워킹 홀리데이 비자를 호주의 학생 비자로 변경할 수 있습니다. 학생 비자 발급 전에 워킹 홀리데이 비자가 만료되면 합법적 인 호주 체류가 가능한 브리징 비자를 받게됩니다.'
      elif haystack.find('student visa')>=0 and haystack.find('study')>=0 and haystack.find('without')>=0:
            haystack='Student visa study without'
            responsek='방문 비자로 최대 12 주 동안 호주에서 공부할 수 있습니다. 12 주 이상 공부하고 싶다면 학생 비자가 있어야합니다.'
      elif haystack.find('working')>=0 and haystack.find('holiday')>=0 and haystack.find('visa')>=0 and haystack.find('stay')>=0:
            haystack='working holiday visa stay'
            responsek='호주 워킹 홀리데이 비자 (Australia Working Holiday Visa)는 한국 및 다른 자격있는 국가의 청소년들이 호주에서 휴가를 보내고 최대 1 년간 일할 수있는 비자입니다. 그러나 특정 요건이 충족되면이 비자는 평생 두 번 부여 될 수 있습니다. 따라서 워킹 홀리데이 비자로 최대 2 년 동안 호주에 머물 수 있습니다.'
      elif haystack.find('working')>=0 and haystack.find('holiday')>=0 and haystack.find('visa')>=0 and haystack.find('long')>=0:
            haystack='working holiday visa long'
            responsek='호주 워킹 홀리데이 비자 (Australia Working Holiday Visa)는 한국 및 다른 자격있는 국가의 청소년들이 호주에서 휴가를 보내고 최대 1 년간 일할 수있는 비자입니다. 그러나 특정 요건이 충족되면이 비자는 평생 두 번 부여 될 수 있습니다. 따라서 워킹 홀리데이 비자로 최대 2 년 동안 호주에 머물 수 있습니다.'
      elif haystack.find('working holiday')>=0 and haystack.find('visa')>=0 and haystack.find('duration')>=0:
            haystack='working holiday visa duration'
            responsek='호주 워킹 홀리데이 비자 (Australia Working Holiday Visa)는 한국 및 다른 자격있는 국가의 청소년들이 호주에서 휴가를 보내고 최대 1 년간 일할 수있는 비자입니다. 그러나 특정 요건이 충족되면이 비자는 평생 두 번 부여 될 수 있습니다. 따라서 워킹 홀리데이 비자로 최대 2 년 동안 호주에 머물 수 있습니다.'
      elif haystack.find('working holiday')>=0 and haystack.find('visa')>=0 and haystack.find('period')>=0:
            haystack='working holiday visa duration'
            responsek='호주 워킹 홀리데이 비자 (Australia Working Holiday Visa)는 한국 및 다른 자격있는 국가의 청소년들이 호주에서 휴가를 보내고 최대 1 년간 일할 수있는 비자입니다. 그러나 특정 요건이 충족되면이 비자는 평생 두 번 부여 될 수 있습니다. 따라서 워킹 홀리데이 비자로 최대 2 년 동안 호주에 머물 수 있습니다.'
      elif haystack.find('study')>=0 and haystack.find('working holiday')>=0 and haystack.find('visa')>=0:
            haystack='working holiday visa study'
            responsek='워킹 홀리데이 비자로 최대 17 주 동안 호주에서 공부할 수 있습니다.'
      elif haystack.find('work')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0 and haystack.find('salary')>=0:
            haystack='work part time salary'
            responsek='현재 호주의 최저 임금은 시간당 AU $ 18.29입니다. 주당 20 시간 일하면 주당 AU $ 365.8을 벌 수 있습니다. 이것은 최저 임금이며 귀하의 직장이나 근무 시간에 따라 이보다 더 많은 것을 얻을 수 있습니다. '
      elif haystack.find('work')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0 and haystack.find('pay')>=0:
            haystack='work part time pay'
            responsek='현재 호주의 최저 임금은 시간당 AU $ 18.29입니다. 주당 20 시간 일하면 주당 AU $ 365.8을 벌 수 있습니다. 이것은 최저 임금이며 귀하의 직장이나 근무 시간에 따라 이보다 더 많은 것을 얻을 수 있습니다.'
      elif haystack.find('work')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0 and haystack.find('earn')>=0:
            haystack='work part time earn'
            responsek='현재 호주의 최저 임금은 시간당 AU $ 18.29입니다. 주당 20 시간 일하면 주당 AU $ 365.8을 벌 수 있습니다. 이것은 최저 임금이며 귀하의 직장이나 근무 시간에 따라 이보다 더 많은 것을 얻을 수 있습니다. '
      elif haystack.find('work')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0 and haystack.find('paid')>=0:
            haystack='work part time paid'
            responsek='현재 호주의 최저 임금은 시간당 AU $ 18.29입니다. 주당 20 시간 일하면 주당 AU $ 365.8을 벌 수 있습니다. 이것은 최저 임금이며 귀하의 직장이나 근무 시간에 따라 이보다 더 많은 것을 얻을 수 있습니다. '
      elif haystack.find('work')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0 and haystack.find('money')>=0:
            haystack='work part time money'
            responsek='현재 호주의 최저 임금은 시간당 AU $ 18.29입니다. 주당 20 시간 일하면 주당 AU $ 365.8을 벌 수 있습니다. 이것은 최저 임금이며 귀하의 직장이나 근무 시간에 따라 이보다 더 많은 것을 얻을 수 있습니다. '
      elif haystack.find('work')>=0 and haystack.find('part')>=0 and haystack.find('time')>=0 and haystack.find('rate')>=0:
            haystack='work part time rate'
            responsek='현재 호주의 최저 임금은 시간당 AU $ 18.29입니다. 주당 20 시간 일하면 주당 AU $ 365.8을 벌 수 있습니다. 이것은 최저 임금이며 귀하의 직장이나 근무 시간에 따라 이보다 더 많은 것을 얻을 수 있습니다. '
      elif haystack.find('work')>=0 and haystack.find('during')>=0 and haystack.find('stud')>=0:
            haystack='work during stud'
            responsek='학생 비자를 소지하고 계시다면, 주당 20 시간을 일할 수 있으며 방학 동안 풀 타임으로 일할 수 있습니다. 그러나 방문 비자로 12 주 미만 만 공부하면 일할 수 없습니다. '
      elif haystack.find('work')>=0 and haystack.find('after')>=0 and haystack.find('graduat')>=0:
            haystack='work after graduat'
            responsek='기본적으로 호주에서 2 년 이상 공부하면 취업 비자를받을 수 있습니다. 학사 또는 석사 학위 (교과 과정) 학위를 취득한 경우 2 년, 연구 석사 학위를 취득한 경우 3 년, 호주에서 박사 학위를 취득한 경우 4 년 동안 취업 비자 (임시 대학원 비자)를받을 수 있습니다. TAFE에서 최소 92 주 과정을 이수하면 18 개월 동안 취업 비자를받을 수 있습니다. 이 경우 MLTSSL에 직업을 지명하고 기술 평가를 통과해야합니다. '
      elif haystack.find('international')>=0 and haystack.find('public')>=0 and haystack.find('school')>=0:
            haystack='international public school'
            responsek='호주에서는 교육부를 통해 학교에 다닐 수 있습니다. 공립학교는 지역에 따라 학업 수준에서 많은 차이가 있기 때문에 생활비가 조금이라도 부담이 되더라도 학업 수준이 높은 학교를 선택하는 것이 좋습니다. '
      elif haystack.find('best')>=0 and haystack.find('universit')>=0:
            haystack='best universit'
            responsek='호주에는 호주 아이비 리그 (Australian Ivy League)라고 불리는 8 개 그룹 (Go8)이 있습니다. 호주 국립 대학교 (ANU), 뉴 사우스 웨일즈 대학교 (UNSW), 퀸즐랜드 대학교 (UQ), 모나 쉬 대학교, 웨스턴 오스트레일리아 대학 (UWA), 시드니 대학교, 애들레이드 대학교 등 8 개 대학이 있습니다 모든 주요 분야에서 우수합니다. 그러나이 대학교 들과는 별도로 특정 전공 분야의 유명한 대학교도 있습니다.'
      elif haystack.find('rank')>=0 and haystack.find('universit')>=0:
            haystack='rank universit'
            responsek='호주에는 호주 아이비 리그 (Australian Ivy League)라고 불리는 8 개 그룹 (Go8)이 있습니다. 호주 국립 대학교 (ANU), 뉴 사우스 웨일즈 대학교 (UNSW), 퀸즐랜드 대학교 (UQ), 모나 쉬 대학교, 웨스턴 오스트레일리아 대학 (UWA), 시드니 대학교, 애들레이드 대학교 등 8 개 대학이 있습니다 모든 주요 분야에서 우수합니다. 그러나이 대학교 들과는 별도로 특정 전공 분야의 유명한 대학교도 있습니다.'
      elif haystack.find('high')>=0 and haystack.find('school')>=0 and haystack.find('australia')>=0 and haystack.find('universit')>=0 and haystack.find('countr')>=0:
            haystack='high school australia universit countr'
            responsek='미국과 같은 SAT가 필요한 국가의 경우 사전에 시험을 준비하고 점수를 제출해야합니다. 국내 대학과 해외 대학이 대학 입학에있어 매우 중요한 요소이므로 일을 철저히 관리하는 것이 좋습니다. '
      elif haystack.find('high')>=0 and haystack.find('school')>=0 and haystack.find('korea')>=0 and haystack.find('universit')>=0 and haystack.find('australia')>=0:
            haystack='high school korea universit australia'
            responsek='호주는 한국과 다른 학문 시스템을 가지고있다. 호주에서는 11-12 학년에 한국 대학 교육의 첫해가 고등학교에서 가르칩니다. 따라서 대부분의 학생들은 한국 대학을 1 년 이상 수료했거나 2 년 이상 한국 단기 대학을 졸업 한 경우에만 호주 대학에 입학 할 수 있습니다. 그러나 고등학교 성적이 아주 좋다면 호주 대학에 직접 입학 할 수 있습니다. '
      elif haystack.find('living')>=0 and haystack.find('year')>=0:
            haystack='living year'
            responsek='당신이 사는 도시와 당신의 생활 방식에 달려 있습니다. 일반적으로 적어도 AU $ 1,200 - AU $ 1,500가 필요합니다. 시드니, 멜버른, 브리즈번 및 소도시와 같은 대도시의 가장 큰 차이점은 임차료입니다. 시드니 스튜디오의 임대료는 주당 450 호주 달러 정도이지만 뉴캐슬 스튜디오 아파트의 경우 주당 AU $ 270입니다.'
      elif haystack.find('living')>=0 and haystack.find('annual')>=0:
            haystack='living annual'
            responsek='당신이 사는 도시와 당신의 생활 방식에 달려 있습니다. 일반적으로 적어도 AU $ 1,200 - AU $ 1,500가 필요합니다. 시드니, 멜버른, 브리즈번 및 소도시와 같은 대도시의 가장 큰 차이점은 임차료입니다. 시드니 스튜디오의 임대료는 주당 450 호주 달러 정도이지만 뉴캐슬 스튜디오 아파트의 경우 주당 AU $ 270입니다.'
      elif haystack.find('tuition')>=0:
            haystack='tuition universit'
            responsek='대학이나 전공 간에는 수업료에 큰 차이가 있습니다. 호주의 최고 명문 대학이라고 불리는 Go8은 연간 약 AU $ 30,000-AU $ 40,000이며, 대도시 밖에 위치한 대학교는 연간 약 AU $ 20,000 -AU $ 35,000입니다. 그러나 의과 대학은 연간 약 AU $ 60,000입니다. '
      elif haystack.find('fee')>=0:
            haystack='fee universit'
            responsek='대학이나 전공 간에는 수업료에 큰 차이가 있습니다. 호주의 최고 명문 대학이라고 불리는 Go8은 연간 약 AU $ 30,000-AU $ 40,000이며, 대도시 밖에 위치한 대학교는 연간 약 AU $ 20,000 -AU $ 35,000입니다. 그러나 의과 대학은 연간 약 AU $ 60,000입니다. '
      elif haystack.find('cours')>=0:
            haystack='undergraduate cours'
            responsek=' '
      elif haystack.find('cours')>=0 and haystack.find('undergrad')>=0:
            haystack='undergraduate cours'
            responsek=' '
      elif haystack.find('credit')>=0:
            haystack='undergraduate credit'
            responsek=' '
      elif haystack.find('credit')>=0 and haystack.find('undergrad')>=0:
            haystack='undergraduate credit'
            responsek=' '
      elif haystack.find('undergraduate')>=0 and haystack.find('duration')>=0:
            haystack='undergraduate duration'
            responsek='3 년 풀 타임 학습'
      elif haystack.find('undergraduate')>=0 and haystack.find('year')>=0:
            haystack='undergraduate year'
            responsek='3 년 풀 타임 학습'
      elif haystack.find('undergraduate')>=0 and haystack.find('long')>=0:
            haystack='undergraduate long'
            responsek='3 년 풀 타임 학습'
      elif haystack.find('cours')>=0:
            haystack='bachelor cours'
            responsek=' '
      elif haystack.find('cours')>=0  and haystack.find('bachelor')>=0:
            haystack='bachelor cours'
            responsek=' '
      elif haystack.find('credit')>=0:
            haystack='bachelor credit'
            responsek=' '
      elif haystack.find('credit')>=0 and haystack.find('bachelor')>=0:
            haystack='undergraduate credit'
            responsek=' '
      elif haystack.find('bachelor')>=0 and haystack.find('duration')>=0:
            haystack='bachelor duration'
            responsek='3 년 풀 타임 학습'
      elif haystack.find('bachelor')>=0 and haystack.find('year')>=0:
            haystack='bachelor year'
            responsek='3 년 풀 타임 학습'
      elif haystack.find('bachelor')>=0 and haystack.find('long')>=0:
            haystack='bachelor long'
            responsek='3 년 풀 타임 학습'
      elif haystack.find('abroad')>=0:
            haystack='abroad'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('overseas')>=0:
            haystack='overseas'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('working holiday')>=0 and haystack.find('age')>=0:
            haystack='working holiday visa age'
            responsek='호주 정부는 워킹 홀리데이 메이커 자격 연령을 30 세에서 35 세까지 연장 할 수있는 시행 방안을 고려하고 있지만, 현재의 자격 연령 (18 세에서 30 세)은 추후 공지가있을 때까지 그대로 유지 될 것입니다. 집행 날짜에 대한 결정적인 발표는 없습니다. '
      elif haystack.find('application')>=0:
            haystack='application'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('apply')>=0:
            haystack='apply'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('commencement')>=0:
            haystack='commencement'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('start')>=0:
            haystack='start'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('enrolment')>=0:
            haystack='enrolment'
            responsek='에서 신청서 및 등록 정보를 찾으십시오. http://www.eduhouse.net/talk/talk_guide_univ.asp'
      elif haystack.find('iae') and haystack.find('eduhouse')>=0:
            haystack='iae eduhouse address'
            responsek='5fl 상경 빌딩, 120 테헤란로드 서울.'
      elif haystack.find('griffith')>=0 and haystack.find('address')>=0:
            haystack='Griffith address'
            responsek='그리피스에는 5 개의 캠퍼스가 있습니다.: Gold Coast campus, Logan campus, Mt Gravatt campus, Nathan campus, and South Bank campus. 어떤 캠퍼스에 가고 싶습니까?'
      elif haystack.find('griffith')>=0 and haystack.find('location')>=0:
            haystack='Griffith location'
            responsek='그리피스에는 5 개의 캠퍼스가 있습니다.: Gold Coast campus, Logan campus, Mt Gravatt campus, Nathan campus, and South Bank campus. 어떤 캠퍼스에 가고 싶습니까?'
      elif haystack.find('griffith')>=0 and haystack.find('locat')>=0:
            haystack='Griffith location'
            responsek='그리피스에는 5 개의 캠퍼스가 있습니다.: Gold Coast campus, Logan campus, Mt Gravatt campus, Nathan campus, and South Bank campus. 어떤 캠퍼스에 가고 싶습니까?'
      elif haystack.find('griffith')>=0 and haystack.find('where')>=0:
            haystack='Griffith where'
            responsek='그리피스에는 5 개의 캠퍼스가 있습니다.: Gold Coast campus, Logan campus, Mt Gravatt campus, Nathan campus, and South Bank campus. 어떤 캠퍼스에 가고 싶습니까?'
      elif haystack.find('nathan')>=0:
            haystack='nathan campus'
            responsek='을 먹었다'
      elif haystack.find('logan')>=0:
            haystack='logan campus'
            responsek=' '
      elif haystack.find('gravatt')>=0:
            haystack='mt gravatt campus'
            responsek=' '
      elif haystack.find('south')>=0 and haystack.find('bank')>=0:
            haystack='south bank campus'
            responsek=' '
      elif haystack.find('gold coast')>=0:
            haystack='gold coast campus'
            responsek=' '
      elif haystack.find('first year')>=0 and haystack.find('australia')>=0 and haystack.find('university')>=0:
            haystack='first year australia university'
            responsek='한국 대학 1 학년과 동등한 기초 프로그램을 마친 후에는 호주 대학의 첫 해를 입력 할 수 있고 졸업장을 치른 후 호주 대학의 2 학년으로 갈 수 있습니다.'
      elif haystack.find('time')>=0 and haystack.find('australia')>=0 and haystack.find('korea')>=0:
            haystack='time difference australia korea'
            responsek='호주와 한국의 시차는 약 30 분에서 1 시간 정도이며 지역마다 조금씩 다릅니다. 예를 들어, 시드니, 멜버른, 브리즈번은 한국보다 1 시간 빠르고 애들레이드는 한국보다 30 분 빠르고 퍼스는 한국보다 1 시간 늦습니다'
      elif haystack.find('undergraduate')>=0:
            haystack='undergraduate'
            responsek='우리가 추천하는 몇 가지 학부 프로그램을 살펴보십시오.: http://www.eduhouse.net/goods/goods_main_theme.asp?natCd=4&ProcCd=2003'
      elif haystack.find('bachelor')>=0:
            haystack='bachelor'
            responsek='우리가 추천하는 몇 가지 학부 프로그램을 살펴보십시오.: http://www.eduhouse.net/goods/goods_main_theme.asp?natCd=4&ProcCd=2003'
      elif haystack.find('campus')>=0:
            haystack='Griffith campus'
            responsek='그리피스에는 5 개의 캠퍼스가 있습니다.: Gold Coast campus, Logan campus, Mt Gravatt campus, Nathan campus, and South Bank campus. 어떤 캠퍼스에 가고 싶습니까?'
      elif haystack.find('address')>=0:
            haystack='Griffith address'
            responsek='그리피스에는 5 개의 캠퍼스가 있습니다.: Gold Coast campus, Logan campus, Mt Gravatt campus, Nathan campus, and South Bank campus. 어떤 캠퍼스에 가고 싶습니까?'
      elif haystack.find('opening hour')>=0 or haystack.find('working hour')>=0:
            haystack='opening hours'
            responsek='대학은 월요일부터 금요일까지 오전 9시에서 오후 5 시까 지 일하고있다.'
      elif haystack.find('degree')>=0:
            haystack='degree'
            responsek='어느 정도의 학위를 소지하고 있습니까 (학사, 석사 또는 박사)?'
      elif haystack.find('postgrad')>=0 or haystack.find('master')>=0 or haystack.find('phd')>=0 or haystack.find('after college')>=0 or haystack.find('college')>=0:
            haystack='postgraduate'
            responsek='또한 그리피스 대학 (Griffith University) 웹 사이트를 통해 대학원 학위를 얻을 수 있습니다: https://www.griffith.edu.au/office-marketing-communications/brochures/postgraduate-degrees-guide'
      elif haystack.find('hi ')>=0:
            haystack='hello'
            responsek='안녕하세요, 어떻게 도와 드릴까요?'
      elif haystack.find('hello ')>=0:
            haystack='hello'
            responsek='안녕하세요, 어떻게 도와 드릴까요?'
      elif haystack.find('how are you')>=0 or haystack.find('understand/ok')>=0:
            haystack='how are you?'
            responsek='고맙습니다'
      elif haystack.find('thank')>=0:
            haystack='thanks'
            responsek='천만에요'
      else:
            haystack='Can you please make your question more specific?'
            responsek=' '


      response2 = bot.get_response(haystack)
      response=str(responsek)+'\n\n'+str(response2)
      print(response2)
      print(responsek)
      print(response)
      return(response)

#response = bot.get_response(entered_input)
#print(response)
