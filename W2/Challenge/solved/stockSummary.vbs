Sub stockSum()

' declare needed variables
Dim lastRow As Long
Dim curOutRow As Integer

Dim ticker As String
Dim curVol As Long
Dim priceOpen As Double
Dim priceClose As Double

' iterate through sheets for data
For Each ws In Worksheets

    ' make destination headers
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Yearly Change"
    ws.Range("K1").Value = "Percent Change"
    ws.Range("L1").Value = "Total Stock Volume"
    
    ws.Range("O2").Value = "Greatest % Increase"
    ws.Range("O3").Value = "Greatest % Decrease"
    ws.Range("O4").Value = "Greatest Total Volume"
    ws.Range("P1").Value = "Ticker"
    ws.Range("Q1").Value = "Value"
    
    ' get lastRow, reset current row
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    curOutRow = 2
    
    ' get first values
    ticker = ws.Cells(2, 1).Value
    priceOpen = ws.Cells(2, 3).Value
        
    ' iterate through data
    For i = 2 To lastRow
        ' add volume to total
        tempVol = ws.Cells(i, 7).Value
        ws.Cells(curOutRow, 12).Value = ws.Cells(curOutRow, 12).Value + tempVol
        
        ' following commented code would store the close price and ticker for the current row -
        ' this seems (?) to be what the rubric suggests, but is much more inefficient than only
        ' grabbing this info once per stock
        ' ticker = ws.Cells(i, 1).Value
        ' priceClose = ws.Cells(i, 6).Value
        
        ' check if new ticker in next row
        If ticker <> ws.Cells(i + 1, 1).Value Then
            ' output ticker
            ws.Cells(curOutRow, 9).Value = ticker
            
            ' grab final closing price
            priceClose = ws.Cells(i, 6).Value
            
            ' calculate yearly change
            Dim yearChange As Double
            yearChange = priceClose - priceOpen
            
            ' output yearly / % change
            ws.Cells(curOutRow, 10).Value = yearChange
            ws.Cells(curOutRow, 11).Value = yearChange / priceOpen
            
            ' format yearly / % change
            If yearChange > 0 Then
                ' green if positive
                ws.Cells(curOutRow, 10).Interior.ColorIndex = 4
                ws.Cells(curOutRow, 11).Interior.ColorIndex = 4
            ElseIf yearChange < 0 Then
                ' red if negative
                ws.Cells(curOutRow, 10).Interior.ColorIndex = 3
                ws.Cells(curOutRow, 11).Interior.ColorIndex = 3
            End If
                        
            ' get next ticker / open price
            ticker = ws.Cells(i + 1, 1).Value
            priceOpen = ws.Cells(i + 1, 3).Value
            
            ' update current output row
            curOutRow = curOutRow + 1
            
        End If
    
    Next i
    
    ' set base values (0) for "Greatest ____" Table
    ' uses first value in results table in case you were to use this on a sheet
    ' of data with only positive / negative stocks
    ws.Range("P2:P4").Value = ws.Range("I2").Value
    ws.Range("Q2").Value = ws.Range("K2").Value
    ws.Range("Q3").Value = ws.Range("K2").Value
    ws.Range("Q4").Value = ws.Range("L2").Value
    
    ' get lastRow for results table
    lastRow = curOutRow - 1
    
    ' iterate through results table, skipping first row since those are the starter values
    For i = 3 To lastRow
        ' check & store greatest % increase
        If ws.Cells(i, 11).Value > ws.Range("Q2").Value Then
            ws.Range("Q2").Value = ws.Cells(i, 11).Value
            ws.Range("P2").Value = ws.Cells(i, 9).Value
        
        End If
        
        ' check & store greatest % decrease
        If ws.Cells(i, 11).Value < ws.Range("Q3").Value Then
            ws.Range("Q3").Value = ws.Cells(i, 11).Value
            ws.Range("P3").Value = ws.Cells(i, 9).Value
        
        End If
        
        ' check & store greatest total vol
        If ws.Cells(i, 12).Value > ws.Range("Q4").Value Then
            ws.Range("Q4").Value = ws.Cells(i, 12).Value
            ws.Range("P4").Value = ws.Cells(i, 9).Value
        
        End If
        
    Next i
    
    ' format column widths, data types
    ws.Columns("I:Q").AutoFit
    ' code from https://www.teachexcel.com/free-excel-macros/m-73,Format-Cells-as-a-Scientific-Number-in-Excel-Number-Formatting.html
    ws.Range("K2:K" & curOutRow).NumberFormat = "0.00%"
    ws.Range("Q2:Q3").NumberFormat = "0.00%"
    ws.Range("Q4").NumberFormat = "0.00E+00"
    
Next ws

End Sub




