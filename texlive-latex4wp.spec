# revision 22314
# category Package
# catalog-ctan /info/latex4wp
# catalog-date 2010-09-15 17:37:36 +0200
# catalog-license fdl
# catalog-version 1.0.7
Name:		texlive-latex4wp
Version:	1.0.7
Release:	7
Summary:	A LaTeX guide specifically designed for word processor users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex4wp
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.7-2
+ Revision: 753131
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0.7-1
+ Revision: 718810
- texlive-latex4wp
- texlive-latex4wp
- texlive-latex4wp
- texlive-latex4wp

