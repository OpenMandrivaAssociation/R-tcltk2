%global packname  tcltk2
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.2.4
Release:          1
Summary:          Tcl/Tk Additions
Group:            Sciences/Mathematics
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/tcltk2_1.2-4.tar.gz
Requires:         R-tcltk 
Requires:         R-utils 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-tcltk
BuildRequires:    R-utils 

%description
A series of additional Tcl commands and Tk widgets with style and various
functions (under Windows: DDE exchange, access to the registry and icon
manipulation) to supplement the tcltk package

%prep
%setup -q -c -n %{packname}
perl -pi -e 's|/bin/tclsh8.3|%{_bindir}/tclsh|;'			\
    tcltk2.Rcheck/tcltk2/tklibs/ctext3.2/function_finder.tcl		\
    tcltk2/inst/tklibs/ctext3.2/function_finder.tcl

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Fonts.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/gui
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/tklibs


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1_5-1
+ Revision: 776343
- Import R-tcltk2
- Import R-tcltk2


