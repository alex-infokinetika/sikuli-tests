����� ������ ��� �������� ������� ����������� ������� (navstat.ru)

��� ���������� ������ ���������� ����������:
JRE7
Sikuli
GIT (�� �������)

��������� ���������� �� ������������ �������� �����

1 ���������� JRE7 - http://www.java.com/ru/download/index.jsp
2 ������� sikuli-setup.jar - https://launchpad.net/sikuli/+download
3 ���������� Sikuli:
	3.1 ������� ����� ��� ��������� - ������ C:\Program Files (x86)\Sikuli X\ ��� ����� �����
	3.2 ����������� sikuli-setup.jar � ���������
	3.3 ������ �� � ����������� ��������� - ������ ��������� ���� runSetup.cmd
	3.4 ��������� runSetup.cmd
	3.5 ������� ����������� ������ - Pack2 ��� ������� ������; Pack1 ��� ��������������
	3.6 ������ �������� �� �� ��� �������
	3.7 ������� ���������� ����� ������������ SIKULI_HOME = ���������� ���� ����������� Sikuli (��� ������� � ����� � �����)
4 � �� ����������� �� ���� ������������ �� git/github, �������� ���������� ����� ������������ GIT_HOME = ���������� � ������� ��������� sikuli-tests (����� � �������, ��������� ��� ������������� git) (�������� GIT_HOME = D:\GitHub)
5 ����� �� ������� � ��������� - ����� ����� ���������� ����������

���������� ������

��� ���������� ������� ������ ������������ HTMLTestRunner
��� ������� ��������� ������ ������ ���� HTMLTestRunner
��� ������� ���� ��������� �������� .bat ������������� � ���������� sikuli-tests
��� ���������� ���� ��������� ���������� ��������� ��������������� .bat
��������� ���������� ���� ��������� ������������ � ���������� � ��� ���� ������������� � ���������� %GIT_HOME%
	��������: ���� �������� smoketest.sikuli ����������� � ������� smoketest.bat � ���������� ��������� � smoketest.html
	��-�� � ������� ��������:
		%GIT_HOME%\sikuli-tests\smoketest.sikuli
		%GIT_HOME%\sikuli-tests\smoketest.bat
		%GIT_HOME%\smoketest.html
����� ������������� �� win7 (��� ������ ��� xp ���������� ���������� ������� �������� ������ � ������ %GitHub%\sikuli-tests\baseFunction.sikuli\clear.bat)
��� ������ ������ ���������� ��������� �� ������ ������ ����� Navstat (����� �� ����� ��������� ��������� ��� ��� ������������� ������)

��������� ������

����� Sikuli ������������� � ������ ���� test_name.sikuli
��� ����� �������� ���������� ���� (test_name.py) � ����� � ����� �������� (��������) (��������� ��� �� ���������)
� ����� %GIT_HOME%\sikuli-tests\img �������� ������� ����������� � ���������� ������ (�� �������� ���������� ������� ��� ������� � ��� �����, �� SikuliIDE ���� ������������, ��� ����������� ��� ������ ����� �������� � ���������� ����� � ��������� �� ���)
