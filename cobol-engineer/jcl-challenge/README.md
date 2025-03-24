# JCL Code Review Exercise

## Background
The JCL job for this coding challenge ([JCL-Code-Challenge.jcl](JCL-Code-Challenge.jcl)) copies the contents of a VSAM file into a variable block QSAM file. Next, a program is executed which converts the contents of the QSAM file into a new (and unspecified) format. File specifications are not relevant for this challenge. The old VSAM file is then deleted and redefined using the file's new specifications. Finally, the contents of the converted QSAM file are copied into the newly defined VSAM file.

## Task
Review JCL job [JCL-Code-Challenge.jcl](JCL-Code-Challenge.jcl) and do the following:

1. **Analyze** the job to gain a better understanding of each step.
2. **Resolve** the coding mistakes found in the program.
3. **Identify** opportunities for improving the job's readability and maintainability.

## Note
The interview team at Oddball recognizes that the time allowed to complete this exercise is limited. The team also does not anticipate the interviewee having the ability to run a JCL scan to identify runtime issues. The expectation is that not every mistake will be caught or opportunity for code improvement explored. However, task prioritization is a major component of this exercise and is something to be mindful of as you work through this challenge. Likewise, manual code tracing and the interviewee's understanding of basic JCL syntax will also be gauged via this exercise.

## Internal Use
Additional information for administering the JCL Code Review Exercise can be found [here](https://drive.google.com/drive/folders/1AI2RkhhZHTCkKirO30i60VgFZQ0u3CPw)