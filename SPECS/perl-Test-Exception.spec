%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Test-Exception
Version:        0.43
Release:        1%{?dist}
Summary:        Test exception-based code
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Exception/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/E/EX/EXODIST/Test-Exception-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006001
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Uplevel) >= 0.18
BuildRequires:  perl(Test::Builder) >= 0.7
BuildRequires:  perl(Test::Builder::Tester) >= 1.07
BuildRequires:  perl(Test::Harness) >= 2.03
BuildRequires:  perl(Test::More) >= 0.7
BuildRequires:  perl(warnings)
Requires:       perl(base)
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(strict)
Requires:       perl(Sub::Uplevel) >= 0.18
Requires:       perl(Test::Builder) >= 0.7
Requires:       perl(Test::Builder::Tester) >= 1.07
Requires:       perl(Test::Harness) >= 2.03
Requires:       perl(warnings)

%description
This module provides a few convenience methods for testing exception
based code. It is built with Test::Builder and plays happily with
Test::More and friends.

%prep
%setup -q -n Test-Exception-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 0.43-1
- Specfile autogenerated by cpanspec 1.78.