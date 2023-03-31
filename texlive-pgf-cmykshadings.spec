Name:		texlive-pgf-cmykshadings
Version:	52635
Release:	2
Summary:	Support for CMYK and grayscale shadings in PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgf-cmykshadings
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-cmykshadings.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-cmykshadings.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-cmykshadings.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for CMYK and grayscale shadings
for the pgf package. By default pgf only supports RGB shadings.
The package attempts to produce shadings consistent with the
currently selected xcolor colour model. The rgb, cmyk, and gray
colour models from the xcolor package are supported. Note: This
package is deprecated since pgf version 3.1.3, since CMYK and
grayscale shadings are now directly supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pgf-cmykshadings
%{_texmfdistdir}/tex/latex/pgf-cmykshadings
%doc %{_texmfdistdir}/doc/latex/pgf-cmykshadings

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
