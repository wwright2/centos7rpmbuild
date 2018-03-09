Name:           perl-Math-Prime-Util
Version:        0.69
Release:        1%{?dist}
Summary:        Utilities related to prime numbers, including fast sieves and factoring
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Prime-Util/
Source0:        http://www.cpan.org/authors/id/D/DA/DANAJ/Math-Prime-Util-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.006002
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::SHA) 
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Test::More) >= 0.45
Requires:       perl(Carp)
Requires:       perl(Config)
Requires:       perl(constant)
Requires:       perl(Digest::SHA) 
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Math::BigInt::GMP)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A module for number theory in Perl. This includes prime sieving, primality
tests, primality proofs, integer factoring, counts / bounds /
approximations for primes, nth primes, and twin primes, random prime
generation, and much more.

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0 

%prep
%setup -q -n Math-Prime-Util-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes cpanfile LICENSE META.json README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Thu Mar 08 2018 Your Name <wwright@nice.com> 0.69-1
- Specfile autogenerated by cpanspec 1.78.
