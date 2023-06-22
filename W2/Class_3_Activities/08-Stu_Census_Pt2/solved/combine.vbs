Sub combineData()

Dim lastRow As Integer
Dim sheetName As String
Dim curRow As Integer

' make destination sheet
Sheets.Add.Name = "Combined_Data"

' copy header & set first row
Worksheets("Combined_Data").Range("A1:K1").Value = Worksheets("2016_census_data").Range("A1:K1").Value
curRow = 2

' iterate through sheets for data
For Each ws In Worksheets
    ' get sheet name
    sheetName = ws.Name
    
    ' iterate through non-destination sheets
    If sheetName <> "Combined_Data" Then
        ' get lastRow
        lastRow = ws.Cells(Rows.Count, 3).End(xlUp).Row
        
        ' iterate through rows, copy data to current row in destination and iterate current row
        For i = 2 To lastRow
            Worksheets("Combined_Data").Range("A" & curRow & ":K" & curRow).Value = ws.Range("A" & i & ":K" & i).Value
            curRow = curRow + 1
        Next i
    
    End If

Next ws

' format column widths
Worksheets("Combined_Data").Columns("A:K").AutoFit

End Sub

