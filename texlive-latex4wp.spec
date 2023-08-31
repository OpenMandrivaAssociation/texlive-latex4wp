Name:		texlive-latex4wp
Version:	68096
Release:	1
Summary:	A LaTeX guide specifically designed for word processor users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex4wp
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex4wp.doc.r%{version}.tar.xz
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
%doc %{_texmfdistdir}/doc/latex/latex4wp

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
