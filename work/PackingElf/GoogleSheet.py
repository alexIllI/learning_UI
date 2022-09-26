from Google_Process import GoogleAPIClient
import pandas as pd

class GoogleSheets(GoogleAPIClient):
    def __init__(self, status = 'DONE', order_number = '12345') -> None:
        self.status = status
        self.order_number = order_number
        # 呼叫 GoogleAPIClient.__init__()，並提供 serviceName, version, scope
        super().__init__(
            'sheets',
            'v4',
            ['https://www.googleapis.com/auth/spreadsheets'],
        )

    def appendWorksheet(self):
        if self.status == 'DONE':
            df=pd.DataFrame(
            {'貨單編號': [self.order_number],
            '狀態': ['DONE'],
            '註記': ['-']}
            )
            self.googleAPIService.spreadsheets().values().append(
                spreadsheetId='1rLRNI3NFeEBVKxP60kbuh6jf3SB-IdqkaYRGxL1VJdk',
                range='工作表1',
                valueInputOption='USER_ENTERED',
                body={
                    'majorDimension': 'ROWS',
                    'values': df.values.tolist()
                },
            ).execute()
            return 0

        elif self.status == 'CLOSES':
            #關轉
            df=pd.DataFrame(
            {'貨單編號': [self.order_number],
            '狀態': ['CLOSED'],
            '註記': ['關轉']}
            )
            self.googleAPIService.spreadsheets().values().append(
                spreadsheetId='1rLRNI3NFeEBVKxP60kbuh6jf3SB-IdqkaYRGxL1VJdk',
                range='工作表1',
                valueInputOption='USER_ENTERED',
                body={
                    'majorDimension': 'ROWS',
                    'values': df.values.tolist()
                },
            ).execute()
            return 1
        
        else:
            #退貨
            df=pd.DataFrame(
            {'貨單編號': [self.order_number],
            '狀態': ['RETURNED'],
            '註記': ['-']}
            )
            self.googleAPIService.spreadsheets().values().append(
                spreadsheetId='1rLRNI3NFeEBVKxP60kbuh6jf3SB-IdqkaYRGxL1VJdk',
                range='工作表1',
                valueInputOption='USER_ENTERED',
                body={
                    'majorDimension': 'ROWS',
                    'values': df.values.tolist()
                },
            ).execute()
            return 2

        

"""if __name__ == '__main__':
    myWorksheet = GoogleSheets()
    myWorksheet.appendWorksheet()"""