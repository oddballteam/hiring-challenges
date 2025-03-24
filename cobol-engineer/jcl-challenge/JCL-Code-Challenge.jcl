//XXXXXXXX JOB (XXXXX),'XXXXX XX',
//    CLASS=X,MSGCLASS=A,
//    REGION=XNOTIFY=XXXXXXX
//*
//************************************************************
//* THIS JCL SERVES AS A CODING CHALLENGE TO BE COMPLETED BY
//* INTERVIEWING CANDIDATES FOR ODDBALL'S COMMON WORKING FILE
//* MAINTAINER (CWFM) CONTRACT.
//*
//* TASK: CLEAN UP THE JCL BELOW, FIX THE ERRORS FOUND 
//*       THROUGHOUT THE JOB, AND SET THE JOB TO RESTART IN
//*       STEP DELDEF.
//************************************************************
//*
//JOBLIB   DD DSN=XXXX.LOAD,DISP=SHR
//*
//**************************************
//*DELETE THE TEMPORARY FILES
//******************************************************
//DELETE1 EXEC PGM=IEFBR14
//*
//DD1          DSN=XX.OLD,
//             DISP=(MOD,DELETE,DELETE),
//             SPACE=(0,0)
//*
//DELETE2 EXEC PGM=IEFBR14
//*
//DD1       DD DSN=XX,NEW,
//             DISP=(MOD,DELETE,DELETE),
//             SPACE=(0,0)
//*
//****************************************************
//*** COPY   THE OLD VSAM FILE
//**************************************************
//BACKUP  EXEC PGM=IDCAMS
//*
//SYSPRINT  DD SYSOUT=*
//*
//IFILE     DD DSN=VSAM.XX,DISP=SHR
//OFILE     DD DSN QSAM.OLD,
//             DISP=(,CATLG,DELETE),
//             UNIT=PERMDA,SPACE=(CYL,(30,10),RLSE),
//             DCB=(RECFM=VB,LRECL=1097,BLKSIZE=0)
//          DD *
        REPRO INFILE(IFILE) OUTFILE(OFILE)
/*
//*
//********************************************************************
//*CONVERT THE OLD FILE USING CONVERT PROGRAM
//********************************************************************
//PROGRAM       PGM=XXXXXXX
//INFILE   DD  DSN=XX.OLD,DISP=SHR
//INFILE   DD  DSN=XX.NEW,
//             DISP=(NEW,CATLG,DELETE),
               UNIT=SYSDA,
//             SPACE=(CYL,(10,5),RLSE),
//             DCB=(RECFM=VB,LRECL=15004,BLKSIZE=0)
//SYSPRINT DD  SYSOUT=*
//*
//****************************************************
//*** DELETE/DEFINE VSAM FILE
//************************************************
//DELDEF   EXEC PGM=      ,COND=(0,NE)
//SYSPRINT  DD SYSOUT=*
//*
//SYSIN     DD *
           DELETE XXXX.FILE

            IF MAXCC  LE 8 THEN DO
               SET LASTCC = 0
               SET MAXCC  = 0
               END
           DEFINE CLUSTER(NAME(XX.FILE)                -
                          CONTROLINTERVALSIZE(4096)    -
                          CYLINDERS(30 10)             -
                          VOLUMES(*)                   -
                          NOERASE                      -
                          INDEXED                      -
                          KEYS(11 0)                   -
                          FREESPACE(10 10)             -
                          RECORDSIZE(78 1093)          -
                          NOREUSE                      -
                          SHAREOPTIONS(2 3)            -
                          NONSPANNED                   -
                          SPEED                        -
                          UNIQUE                       -
                          NOWRITECHECK)                -
                  DATA(NAME(XX.FILE.DATA))             -
                  INDEX(NAME(XX.FILE.INDEX)            -
                          CONTROLINTERVALSIZE(512))
/*
//****************************************************
//*** COPY THE CONVERTED NEW FILE TO VSAM FILE
//****************************************************
//*
//BACKUP  EXEC PGM=IDCAMS
//*
//SYSPRINT  DD SYSOUT=*
//*
//FILE1     DD DSN=XX.NEW,DISP=SHR
//FILE2     DD DSN=XX.VSAM,DISP=SHR
//SYSIN     DD *
        REPRO INFILE(FILE1) OUTFILE(FILE2)
/
//**********************************************************