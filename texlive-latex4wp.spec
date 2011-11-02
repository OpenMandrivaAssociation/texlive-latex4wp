Name:		texlive-latex4wp
Version:	1.0.7
Release:	1
Summary:	A LaTeX guide specifically designed for word processor users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex4wp
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
"LaTeX for Word Processor Users" is a guide that helps
converting knowledge and techniques of word processing into the
LaTeX typesetting environment. It aims at helping WP users use
LaTeX instead.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex4wp/HOW-TO-TYPESET
%doc %{_texmfdistdir}/doc/latex/latex4wp/README
%doc %{_texmfdistdir}/doc/latex/latex4wp/dat2tex
%doc %{_texmfdistdir}/doc/latex/latex4wp/exa.sty
%doc %{_texmfdistdir}/doc/latex/latex4wp/gnuplot.gp
%doc %{_texmfdistdir}/doc/latex/latex4wp/gnuplot.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp/latex4wp.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp/latex4wp.tex
%doc %{_texmfdistdir}/doc/latex/latex4wp/midifile.mid
%doc %{_texmfdistdir}/doc/latex/latex4wp/small.eepic
%doc %{_texmfdistdir}/doc/latex/latex4wp/small.eps
%doc %{_texmfdistdir}/doc/latex/latex4wp/small.fig
%doc %{_texmfdistdir}/doc/latex/latex4wp/small.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp/small.pdf_t
%doc %{_texmfdistdir}/doc/latex/latex4wp/tbx.eps
%doc %{_texmfdistdir}/doc/latex/latex4wp/tbx.pdf
%doc %{_texmfdistdir}/doc/latex/latex4wp/tbx.tex
%doc %{_texmfdistdir}/doc/latex/latex4wp/xfig.eps
%doc %{_texmfdistdir}/doc/latex/latex4wp/xfig.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
