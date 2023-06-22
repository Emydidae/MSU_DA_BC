Sub SentenceBreaker()

    ' Retrieve the user sentence and store in variable
    ' <YOUR CODE GOES HERE>
    Dim Sentence As String
    Sentence = Range("B1").Value
    
    ' Retrieve the user word numbers and store in variables
    ' <YOUR CODE GOES HERE>
    Dim Word1 As Integer
    Dim Word2 As Integer
    Dim Word3 As Integer
    Word1 = Range("A4").Value
    Word2 = Range("A5").Value
    Word3 = Range("A6").Value


    ' Split the user's sentence into words
    ' <YOUR CODE GOES HERE>
    Dim Words() As String
    Words = Split(Sentence, " ")


    ' Use the word numbers to retrieve the specific words in the sentence
    ' Remember to offset by the 0 index
    ' <YOUR CODE GOES HERE>
    Range("B4").Value = Words(Word1 - 1)
    Range("B5").Value = Words(Word2 - 1)
    Range("B6").Value = Words(Word3 - 1)
    
    MsgBox ("The" + Str(Word1) + "rd word is " + Words(Word1 - 1))

End Sub
