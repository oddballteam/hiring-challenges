       ID DIVISION.
       PROGRAM-ID.    CODECHAL.
      *AUTHOR.        JORDAN FIRARI
      *DATE-WRITTEN.  MARCH 06, 2025.
      *****************************************************************
      *
      * THIS PROGRAM SERVES AS A CODING CHALLENGE TO BE COMPLETED BY
      * INTERVIEWING CANDIDATES FOR ODDBALL'S COMMON WORKING FILE
      * MAINTAINER (CWFM) CONTRACT.
      *
      *****************************************************************
      *************** M A I N T E N A N C E   N O T E S ***************
      ***%************************************************************:
      ***%CCR#      :                      PROGRAMMER: JORDAN FIRARI
      ***%MODLOG TAG:                      COMPANY   : ODDBALL
      ***%RELEASE NO:                      DATE      : 03/06/2025
      ***%
      ***%PROBLEM   : NEED A CODING CHALLENGE FOR CWFM SOFTWARE
      ***%            ENGINEER INTERVIEWS.
      ***%
      ***%SOLUTION  : INITIAL CREATION
      ***%************************************************************:
      *********** E N D   M A I N T E N A N C E   N O T E S ***********
      *****************************************************************
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT  TESTI-FILE      ASSIGN  TESTI
                                   STATUS  TESTI-STATUS.
           SELECT  TESTO-FILE      ASSIGN  TESTO
                                           TESTO-STATUS.
       DATA DIVISION.
       FILE SECTION.

       FD  TESTI-FILE
           RECORDING F
           BLOCK 0 RECORDS.

       01  TESTI-RECORD.
           05  TESTI-KEY                   PIC  X(03).
           05  TESTI-FILLER                PIC  X(77).

       FD  TESTO-FILE
           RECORDING F
           BLOCK 0 RECORDS.

       01  TESTO-RECORD.
           05  TESTO-KEY                   PIC  X(03).
           05  TESTO-FILLER1               PIC  X(01).
           05  TESTO-DATE                  PIC  9(08).
           05  TESTO-FILLER2               PIC  X(01).
           05  TESTO-AMT                   PIC  9(07).99.
           05  TESTO-FILLER3               PIC  X(01).
           05  TESTO-CATEGORY              PIC  9(04).
           05  TESTO-FILLER4               PIC  X(52).

       WORKING-STORAGE SECTION.

       01 WORK-FIELDS.
           05  TESTI-STATUS                PIC  X(02).
               88  TESTI-SUCCESS                VALUE ZERO.
               88  TESTI-EOF                    VALUE '10'.
           05  WS-LOOP-CNT                 PIC 99.
       01 WORK-TABLES.
           05  WS-LOOKUP-TABLE.
               10  WS-LU-ENTRY OCCURS 20 TIMES INDEXED BY WS-LU-NDX.
                   15  WS-LU-KEY           PIC  X(03).
                   15  WS-LU-DATE          PIC  9(08).
                   15  WS-LU-AMT           PIC  9(07)V99.

       PROCEDURE DIVISION.

      ******************************************************************
      * MAIN OPERATIONS PARAGRAPH FOR PROGRAM.
      ******************************************************************
       0000-MAINLINE.
      *LOTS OF CLEAN UP OPPORTUNITIES
      *  -BREAK UP INTO LOGICAL PARAGRAPHS
      *  -LINE UP EXECUTABLE STATEMENTS
      *  -LINE UP TO'S AND THRU'S
      *  -CREATE MORE WHITE SPACE
           OPEN INPUT TESTI-FILE
           OPEN OUTPUT TESTO-FILE
      *BETTER WAYS OF INITIALIZING THIS DATA
           MOVE 'ABC' TO WS-LU-KEY(1)
           MOVE 'BCD' TO WS-LU-KEY(2)
           MOVE 'CDE' TO WS-LU-KEY(3)
           MOVE 'DEF' TO WS-LU-KEY(4)
           MOVE 'ZYX' TO WS-LU-KEY(5)
           MOVE 'FGH' TO WS-LU-KEY(6)
           MOVE 'GHI' TO WS-LU-KEY(7)
           MOVE 'HIJ' TO WS-LU-KEY(8)
           MOVE 'IJK' TO WS-LU-KEY(9)
           MOVE 'JKL' TO WS-LU-KEY(10)
           MOVE 'KLM' TO WS-LU-KEY(11)
           MOVE 'CBA' TO WS-LU-KEY(12)
           MOVE 'MNO' TO WS-LU-KEY(13)
           MOVE 'NOP' TO WS-LU-KEY(14)
           MOVE 'OPQ' TO WS-LU-KEY(15)
           MOVE 'PQR' TO WS-LU-KEY(16)
           MOVE 'QRS' TO WS-LU-KEY(17)
           MOVE 'DCB' TO WS-LU-KEY(18)
           MOVE 'STU' TO WS-LU-KEY(19)
           MOVE 'TUV' TO WS-LU-KEY(20)
           MOVE 20250306 TO WS-LU-DATE(1)
           MOVE 20250307 TO WS-LU-DATE(2)
           MOVE 20250308 TO WS-LU-DATE(3)
           MOVE 20250315 TO WS-LU-DATE(4)
           MOVE 20250310 TO WS-LU-DATE(5)
           MOVE 20250311 TO WS-LU-DATE(6)
           MOVE 20250312 TO WS-LU-DATE(7)
           MOVE 20250313 TO WS-LU-DATE(8)
           MOVE 20250320 TO WS-LU-DATE(9)
           MOVE 20250315 TO WS-LU-DATE(10)
           MOVE 20250316 TO WS-LU-DATE(11)
           MOVE 20250317 TO WS-LU-DATE(12)
           MOVE 20250318 TO WS-LU-DATE(13)
           MOVE 20250326 TO WS-LU-DATE(14)
           MOVE 20250320 TO WS-LU-DATE(15)
           MOVE 20250321 TO WS-LU-DATE(16)
           MOVE 20250322 TO WS-LU-DATE(17)
           MOVE 20250330 TO WS-LU-DATE(18)
           MOVE 20250324 TO WS-LU-DATE(19)
           MOVE 20250301 TO WS-LU-DATE(20)
           MOVE 100000 TO WS-LU-AMT(1)
           MOVE 120000 TO WS-LU-AMT(2)
           MOVE 80000 TO WS-LU-AMT(3)
           MOVE 70000 TO WS-LU-AMT(4)
           MOVE 90000 TO WS-LU-AMT(5)
           MOVE 50000 TO WS-LU-AMT(6)
           MOVE 140000 TO WS-LU-AMT(7)
           MOVE 30000 TO WS-LU-AMT(8)
           MOVE 20000 TO WS-LU-AMT(9)
           MOVE 1110000 TO WS-LU-AMT(10)
           MOVE 19000 TO WS-LU-AMT(11)
           MOVE 8000 TO WS-LU-AMT(12)
           MOVE 7000 TO WS-LU-AMT(13)
           MOVE 26000 TO WS-LU-AMT(14)
           MOVE 5000 TO WS-LU-AMT(15)
           MOVE 44000 TO WS-LU-AMT(16)
           MOVE 3000 TO WS-LU-AMT(17)
           MOVE 32000 TO WS-LU-AMT(18)
           MOVE 1000 TO WS-LU-AMT(19)
           MOVE 900 TO WS-LU-AMT(20)
           PERFORM UNTIL TESTI-EOF
      *CHECK FOR SUCCESSFUL FILE READ BEFORE PROCESSING RECORD
             READ TESTI-FILE
      *TYPO IN PERFORM
      *LOOP IS NOT NEEDED
                   PEROFRM VARYING WS-LOOP-CNT FROM 1 BY 1
                           UNTIL WS-LOOP-CNT >= 20
                       SEARCH WS-LU-ENTRY
                         AT END
      *NEXT SENTENCE WILL SEND CONTROL TO END OF PROGRAM
                               NEXT SENTENCE
                           WHEN TESTI-KEY = WS-LU-KEY(WS-LU-NDX)
                               MOVE WS-LU-KEY(WS-LU-NDX) TO TESTO-KEY
                               MOVE WS-LU-DATE(WS-LU-NDX) TO TESTO-DATE
                               MOVE WS-LU-AMT(WS-LU-NDX) TO TESTO-AMT
                              EVALUATE TRUE
      *AVOID HARD CODED VALUES
                                  WHEN TESTO-DATE > 20250315 AND
                                       TESTO-AMT > 10000
      *TESTO-CATEGORY IS A NUMERIC FIELD
                                      MOVE "9876" TO TESTO-CATEGORY
                                WHEN OTHER
                                  MOVE "0000" TO TESTO-CATEGORY
                              END-EVALUATE
      *TESTO-RECORD WAS NEVER INITIALIZED
                              WRITE TESTO-RECORD
                       END-SEARCH
                   END-PERFORM
           END-PERFORM
      *CLOSE TESTI AND TESTO
           GOBACK.
       0000-EXIT.
           EXIT.