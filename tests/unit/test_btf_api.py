from unittest import mock, TestCase
from botfriend_api import BotfriendData, Botfriend


class TestBotfriendApi(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    
    def test_look_for_i_creates_string_with_i_converted(self):

        msg = "i am sending a message"
        btf_data = BotfriendData()
        btf = Botfriend(btf_data)
        
        list_msg = 'I am sending a message'
        result = btf.look_for_i(msg)
        
        self.assertEqual(list_msg, result)


    





