Sub censusForm()

Dim sheetName() As String
Dim lastRow As Integer
Dim currentPlace() As String

For Each ws In Worksheets
    ' get sheet name
    sheetName() = Split(ws.Name, "_")
    
    ' make new 1st column titled year
    ws.Range("A1").EntireColumn.Insert
    ws.Cells(1, 1).Value = "Year"
    ws.Cells(1, 1).Font.Bold = True
    
    ' make new 2nd column titled county & rename 3rd column
    ws.Range("B1").EntireColumn.Insert
    ws.Cells(1, 2).Value = "County"
    ws.Cells(1, 2).Font.Bold = True
    ws.Cells(1, 3).Value = "State"
    
    ' get lastRow
    lastRow = ws.Cells(Rows.Count, 3).End(xlUp).Row
    
    ' iterate through data
    For i = 2 To lastRow
        ' put year in 1st col
        ws.Cells(i, 1).Value = sheetName(0)
        
        ' get info for place and split, put in respective columns
        currentPlace() = Split(ws.Cells(i, 3).Value, ", ")
        ws.Cells(i, 2).Value = currentPlace(0)
        ws.Cells(i, 3).Value = currentPlace(1)
        
        ' format household & per capita to currency
        ws.Cells(i, 6).Style = "Currency"
        ws.Cells(i, 7).Style = "Currency"
    Next i
    
    ' format column widths
    ws.Columns("A:C").AutoFit
Next ws

End Sub