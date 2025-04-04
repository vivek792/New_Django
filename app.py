import unittest
from unittest.mock import patch, MagicMock
import Peyto_PHASE1  # Import the script module (path to the testing script)

class TestScript(unittest.TestCase):
    
    @patch('script.MySQLdb.connect')
    def test_insert_query_phase1result(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Call the function to test
        script.insert_query_phase1result('192.168.1.1', 'hostname1', 'Success', '2024-09-11 12:00:00')
        
        # Assert the correct SQL command was executed
        mock_cursor.execute.assert_called_once_with(
            'INSERT INTO app_phase1peytoresult (IPv4Address,HostName,Status,Date) VALUES (%s, %s, %s, %s)',
            ('192.168.1.1', 'hostname1', 'Success', '2024-09-11 12:00:00')
        )
        mock_connect.return_value.commit.assert_called_once()
    
    @patch('script.ConnectHandler')
    def test_connection_request_success(self, mock_connect_handler):
        # Mock the ConnectHandler
        mock_net_connect = MagicMock()
        mock_connect_handler.return_value = mock_net_connect
        
        # Mock the function to not fail on exceptions
        mock_net_connect.send_command_timing.return_value = "show media"
        mock_net_connect.send_command.return_value = "some output"

        # Mock external function calls within Main_Script_Execution_phase1
        with patch('script.Main_Script_Execution_phase1') as mock_main:
            script.connection_request('192.168.1.1', 'hostname1')
            mock_main.assert_called_once_with('192.168.1.1', 'hostname1', mock_net_connect)
            mock_net_connect.disconnect.assert_called_once()

    @patch('script.MySQLdb.connect')
    def test_insert_into_successlist(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Mock data fetching
        mock_cursor.fetchall.return_value = [
            ('192.168.1.1', 'hostname1', 'Success'),
            ('192.168.1.2', 'hostname2', 'Failed')
        ]

        # Call the function to test
        script.insert_into_successlist()
        
        # Assert the correct SQL command was executed
        mock_cursor.execute.assert_called_with(
            "INSERT INTO app_singleip2and3upgrade(IPv4Address,HostName,Status) VALUES (%s,%s,%s)",
            ('192.168.1.1', 'hostname1', 'Success')
        )
        mock_connect.return_value.commit.assert_called_once()

    @patch('script.MySQLdb.connect')
    def test_inert_into_dataofphase1(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Call the function to test
        script.inert_into_dataofphase1()
        
        # Assert the correct SQL command was executed
        mock_cursor.execute.assert_called_once_with(
            'INSERT INTO app_phase1peytoresult1 (IPv4Address,HostName,Status,Date) SELECT IPv4Address,HostName,Status,Date FROM app_phase1peytoresult'
        )
        mock_connect.return_value.commit.assert_called_once()
    
    @patch('script.MySQLdb.connect')
    def test_truncatetable(self, mock_connect):
        # Mock the database connection and cursor
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        # Call the function to test
        script.truncatetable()
        
        # Assert the correct SQL command was executed
        mock_cursor.execute.assert_called_once_with('TRUNCATE TABLE app_phase1peytoresult')
        mock_connect.return_value.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
