'''
Created on Jun 9, 2019
Ch08
@author: Burkhard
'''

class I18N():
    '''Internationalization'''
    def __init__(self, language):      
        if   language == 'en': self.resourceLanguageEnglish()
        elif language == 'ko': self.resourceLanguageKorean()
        else: raise NotImplementedError('Unsupported language.')
        
    def resourceLanguageEnglish(self):
        self.title = "Python Graphical User Interface"
        
        self.file  = "File"
        self.new   = "New"
        self.exit  = "Exit"
        self.help  = "Help"
        self.about = "About"
        
        self.WIDGET_LABEL = ' Widgets Frame '
        
        self.disabled  = "Disabled"
        self.unChecked = "UnChecked"
        self.toggle    = "Toggle"
        
        # Radiobutton list
        self.colors   = ["Blue", "Gold", "Red"]
        self.colorsIn = ["in Blue", "in Gold", "in Red"]
        
        self.labelsFrame  = ' Labels within a Frame '
        self.chooseNumber = "Choose a number:"
        self.label2       = "Label 2"
        
        self.timeZones = "All Time Zones"
        self.localZone = "Local Zone"
        self.getTime   = "New York"
        
        self.mgrFiles = ' Manage Files '
        
        self.browseTo = "Browse to File..."
        self.copyTo   = "Copy File To :   "
        
    
    def resourceLanguageKorean(self):
        self.title = '그래픽 사용자 인터페이스'                      # w/out umlaut
#         self.title = 'Python Grafische Benutzeroberfl' + "\u00E4" + 'che'       # with umlaut via Unicode
        self.title = '그래픽 사용자 인터페이스'                       # with umlaut UTF-8
        
        self.file  = "파일"
        self.new   = "새로만들기"
        self.exit  = "종류"
        self.help  = "도움말"
        self.about = "\u00DC" + "정보"
        self.about = "정보"

        self.WIDGET_LABEL = ' 위젯 프레임 '
        
        self.disabled  = "비활성화"
        self.unChecked = "미체크"
        self.toggle    = "토글"
        
        # Radiobutton list
        self.colors   = ["파랑", "노랑", "빨강"]
        self.colorsIn = ["내부 파랑", "내부 노랑", "내부 빨강"]
        
        self.labelsFrame  = ' 라벨 프레임 '
        self.chooseNumber = "숫자 선택"
        self.label2       = "라벨 2"
        
        self.timeZones = "모든 지역"
        self.localZone = "해당 지역"
        self.getTime   = "뉴욕"
    
        self.mgrFiles = ' 파일 관리 '
        
        self.browseTo = "파일 찾기... "
        self.copyTo   = "파일 복사하기:     "

#=================================================
if __name__ == '__main__':    
    language = 'en'
    inst = I18N(language)    
    print(inst.title)
    
    language = 'ko'
    inst = I18N(language)    
    print(inst.title)








