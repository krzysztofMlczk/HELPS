%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% File:     aghdpl.cls           (LaTeX Document class option "aghdpl")
%          
% Author:  Marcin Szpyrka     (mszpyrka@agh.edu.pl)
%          Grzegorz J. Nalepa (gjn@agh.edu.pl)
%          AGH University of Science and Technology, Kraków, POLAND
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\message{*** [aghdpl.cls] ---  (MSz, GJN)  v0.1 <03.03.2009>  ***}       

\newif\ifpdflatex\pdflatexfalse
\NeedsTeXFormat{LaTeX2e} % 
\ProvidesClass{aghdpl} 
\DeclareOption{pdflatex}{\pdflatextrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}} 
\ProcessOptions\LoadClass[a4paper,twoside]{report} 

\RequirePackage{times}
\RequirePackage[T1]{fontenc}
\RequirePackage{graphicx}
\RequirePackage{geometry}
\RequirePackage[usenames]{color}
\RequirePackage{fancyhdr}
\RequirePackage{url}
\RequirePackage{titlesec}
\RequirePackage{tocloft}

\geometry{lmargin=30mm, rmargin=20mm, tmargin=25mm, bmargin=25mm, foot=10mm, head=10mm}
\definecolor{Green}{rgb}{0.1,0.5,0.1}

\def\shorttitlePL#1   {\gdef\@shorttitlePL{#1}}
\def\shorttitleEN#1   {\gdef\@shorttitleEN{#1}}
\def\shortauthor#1    {\gdef\@shortauthor{#1}}
\def\titlePL#1        {\gdef\@titlePL{#1}}
\def\titleEN#1        {\gdef\@titleEN{#1}}
\def\facultyEN#1      {\gdef\@facultyEN{#1}}
\def\facultyPL#1      {\gdef\@facultyPL{#1}}
\def\thesistypePL#1   {\gdef\@thesistypePL{#1}}
\def\thesistypeEN#1   {\gdef\@thesistypeEN{#1}}
\def\supervisorPL#1   {\gdef\@supervisorPL{#1}}
\def\supervisorEN#1   {\gdef\@supervisorEN{#1}}
\def\acknowledgements#1   {\gdef\@acknowledgements{#1}}
\def\contentsname{Spis tre\'sci}
\def\listfigurename{Spis rysunk\'ow}
\def\listtablename{Spis tabel}
\def\bibname{Bibliografia}
\def\figurename{Rysunek}
\def\tablename{Tabela}
\def\chaptername{Rozdzia\l{}}
\def\appendixname{Dodatek}
\def\partname{Cz\k{e}\'s\'c}
\def\abstractname{Streszczenie}
% \thesisheaders
% 
% \pagestyle{fancy}
%
%\bibliographystyle{abbrv}
%
%------------------------------------------------------------------------------

\newcommand{\titlepages}{%

\newpage \titlepage 

\begin{center}

{\sffamily{\Large{\bfseries{\textsc Akademia Ekonomiczno-Humanistyczna w Warszawie
}}}

\vspace*{1mm}\rule{\textwidth}{1mm}\vspace*{1mm}

{\large \@facultyPL}}\vspace*{1cm}

\ifpdflatex\includegraphics[scale=0.3]{logo_pl.png}
\else\includegraphics[scale=0.7]{logo_pl.png}
\fi
\vspace*{1cm}

{\huge\scshape \@thesistypePL}\\\vspace*{2cm}

{\LARGE\scshape \@author}\\\vspace*{2mm}
{\large studia niestacjonarne}\\
{\large nr albumu 48715}\\\vspace*{2cm}

{\LARGE{\bfseries\scshape \@titlePL}}\\\vspace*{3cm}

\begin{flushright}
\begin{minipage}[!h]{6cm} 
\large{\scshape Promotor:}\\ \@supervisorPL
\end{minipage}
\end{flushright}

\vfill{\Large Warszawa\\\vspace*{1mm} \@date}

\end{center}

\clearpage \titlepage \vspace*{15cm} \vfill

%\begin{flushright}
%\begin{minipage}[!h]{12cm}
%\mbox{\large{\scshape \textbf{O\'SWIADCZENIE AUTORA PRACY}}}\\[3mm] 
%{\scshape O\'swiadczam, \'swiadomy odpowiedzialno\'sci karnej za po\'swiadczenie nieprawdy, \.ze niniejsz\k{a} prac\k{e} dyplomow\k{a} wykona\l{}em osobi\'scie i samodzielnie, i nie korzysta\l{}em ze \'zr\'ode\l{} innych ni\.z wymienione w pracy.}\\
%\end{minipage}
%
%\vspace{2cm}

%\makebox[6cm][s]{\dotfill}\par
%\makebox[6cm][c]{\small PODPIS}
%
%\end{flushright}

%\clearpage \titlepage
%
%\begin{center}
%
%{\sffamily{\Large{\bfseries{\textsc University of Economics and Human Sciences in Warsaw\\
%}}}
%
%\vspace*{1mm}\rule{\textwidth}{1mm}\vspace*{1mm}
%
%{\large \@facultyEN}}\vspace*{1cm}
%
%\ifpdflatex\includegraphics[scale=0.3]{logo_en.png}
%\else\includegraphics[scale=0.7]{logo_en.png}
%\fi
%\vspace*{1cm}
%
%{\huge\scshape \@thesistypeEN}\\\vspace*{2cm}
%
%{\LARGE\scshape \@author}\\\vspace*{2cm}
%
%{\LARGE{\bfseries\scshape \@titleEN}}\\\vspace*{3cm}

%\begin{flushright}
%\begin{minipage}[!h]{6cm} 
%\large{\scshape Supervisor:}\\ \@supervisorEN
%\end{minipage}
%\end{flushright}

%\vfill{\Large Warsaw \@date}

%\end{center}

%\clearpage \titlepage

%\vspace*{15cm} \vfill
%\begin{flushright} 
%\begin{minipage}[!h]{8cm}
%{\Large \@acknowledgements}
%\end{minipage}
%\end{flushright}

\clearpage

\setcounter{page}{3}

}

\def\thesisheaders{
\fancyfoot[R]{\small \@shortauthor\quad\textit{\@shorttitlePL}}
}

\DeclareOption{en}{
\def\thesisheaders{
\fancyfoot[R]{\small \@shortauthor\quad\textit{\@shorttitleEN}}
}
}

\ProcessOptions

\pagestyle{fancy}
\renewcommand{\chaptermark}[1]{\markboth{\thechapter.\ #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection.\ #1}}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}
\fancyhf{}
\fancyhead{}
\fancyhead[L]{\slshape{\small \rightmark}}
\fancyhead[R]{\bfseries \thepage}

\thesisheaders

\frenchspacing
\sloppy 
\widowpenalty     9999 
\clubpenalty      9999 
\flushbottom

%---------------------------------------------------------------------------
% Ustawienia parametrów dla tytu³ów rozdzia³ów, podrozdzia³ów, itd.
%---------------------------------------------------------------------------
\titleformat{name=\chapter,numberless}[block]
{\bfseries\LARGE} % Styl dla nienumerowanego rozdziału
{\filcenter} % Nie wyświetlaj numeru
{0pt} % Brak odstępu przed tytułem
{\filcenter\bfseries\LARGE} % Wyśrodkowanie i styl tytułu

\titleformat{\chapter}[block]
{\bfseries\Huge} % Styl dla "Rozdział 4"
{\filcenter Rozdzia\l {} \thechapter \\} % Treść nagłówka pierwszej linijki
{1ex} % Odstęp między linijkami
{\filcenter\bfseries\LARGE} % Styl dla tytułu rozdziału (druga linijka)
[{\vspace{-1.5ex}}]


%odstêpy: lewy, góra, dó³
\titlespacing{\chapter}{0pt}{17mm}{19mm}
\titleformat{\section}[block]
{\bfseries\Large}{\filright \Large\thesection. }{0ex}{}
\titlespacing{\section}{7mm}{8mm plus 0mm minus 1mm}{4mm plus 0mm minus 1mm}
\titleformat{\subsection}[block]
{\bfseries\large}{\filright \large\thesubsection. }{0ex}{}
\titlespacing{\subsection}{7mm}{6mm}{2.5mm}
\titleformat{\subsubsection}[block]
{\bfseries\normalsize}{\filright \normalsize\thesubsubsection. }{0ex}{}
\titlespacing{\subsubsection}{7mm}{3mm}{1.5mm}

%---------------------------------------------------------------------------
% Ustawienia parametrów generowania spisu tre¶ci i spisu rysunków
%---------------------------------------------------------------------------

% ===============================
% SPIS TREŚCI
% ===============================
\renewcommand{\cfttoctitlefont}{\bfseries\LARGE}
\renewcommand{\cftbeforetoctitleskip}{20mm}
\renewcommand{\cftaftertoctitleskip}{19mm}
\renewcommand{\cftchapdotsep}{4}
\renewcommand{\cftsecdotsep}{4}
\renewcommand{\cftsubsecdotsep}{4}
\renewcommand{\cftchapleader}{\cftdotfill{\cftchapdotsep}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftsecdotsep}}
\renewcommand{\cftsubsecleader}{\cftdotfill{\cftsubsecdotsep}}
\renewcommand{\cftchapaftersnum}{.}
\renewcommand{\cftsecaftersnum}{.}
\renewcommand{\cftsubsecaftersnum}{.}

% ===============================
% SPIS RYSUNKÓW
% ===============================
\renewcommand{\cftloftitlefont}{\bfseries\LARGE}
%\renewcommand{\cftbeforeloftitleskip}{20mm}
%\renewcommand{\cftafterloftitleskip}{19mm}
%\renewcommand{\cftlofleader}{\cftdotfill{\cftdot}}

% ===============================
% SPIS TABEL
% ===============================
\renewcommand{\cftlottitlefont}{\bfseries\LARGE}
%\renewcommand{\cftbeforelottitleskip}{20mm}
%\renewcommand{\cftafterlottitleskip}{19mm}
%\renewcommand{\cftlotleader}{\cftdotfill{\cftdot}}

% ===============================
% LISTA ALGORYTMÓW

% ===============================
%\renewcommand{\cftbeforeloatitleskip}{20mm}
%\renewcommand{\cftafterloatitleskip}{19mm}
%\renewcommand{\cftloaleader}{\cftdotfill{\cftdot}}
%\renewcommand{\cftloadotsep}{1}

% ===============================
% OPCJONALNIE: globalna gęstość kropek 
% (dla wszystkich spisów naraz)
% ===============================
\renewcommand{\cftdotsep}{4}
