%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Archive-Zip
Version:        1.60
Release:        1%{?dist}
Summary:        Provide an interface to ZIP archive files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Archive-Zip/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/P/PH/PHRED/Archive-Zip-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.017
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Local)
Requires:       perl(Compress::Raw::Zlib) >= 2.017
Requires:       perl(File::Basename)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(File::Path)
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(File::Temp)
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Requires:       perl(IO::Seekable)
Requires:       perl(Time::Local)

%description
The Archive::Zip module allows a Perl program to create, manipulate, read,
and write Zip archive files.

%prep
%setup -q -n Archive-Zip-%{version}

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
%doc Changes META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 1.60-1
- Specfile autogenerated by cpanspec 1.78.